// 全局设备检测和响应式适配
function closePanel(panelId) {
    console.log('[关闭面板] 关闭面板:', panelId);
    const panel = document.getElementById(panelId);
    if (panel) {
        panel.style.display = 'none';
        if (panelId === 'output-panel') {
            if (typeof pollingInterval !== 'undefined' && pollingInterval) {
                clearInterval(pollingInterval);
                pollingInterval = null;
            }
            currentTaskId = null;
        } else if (panelId === 'tunnel-panel' && typeof tunnelPollInterval !== 'undefined' && tunnelPollInterval) {
            clearInterval(tunnelPollInterval);
            tunnelPollInterval = null;
        }
    }
}

function closeTunnelPanel() {
    console.log('[按钮点击] 关闭隧道面板');
    const panel = document.getElementById('tunnel-panel');
    if (panel) {
        panel.style.display = 'none';
        if (typeof tunnelPollInterval !== 'undefined' && tunnelPollInterval) {
            clearInterval(tunnelPollInterval);
            tunnelPollInterval = null;
        }
    }
}

function detectDevice() {
    const ua = navigator.userAgent.toLowerCase();
    const width = window.innerWidth;
    const height = window.innerHeight;
    
    let deviceType = 'desktop';
    let deviceInfo = '';
    
    // 检测移动设备类型
    const mobileDevices = {
        'android': /android/i.test(ua),
        'iphone': /iphone|ipad|ipod/i.test(ua),
        'ipad': /ipad/i.test(ua),
        'wechat': /micromessenger/i.test(ua),
        'weibo': /weibo/i.test(ua),
        'qq': /qq\//i.test(ua),
        'mobile': /mobile|android|iphone|ipad|ipod/i.test(ua)
    };
    
    // 根据屏幕宽度判断设备类型
    if (width < 576) {
        deviceType = 'phone';
    } else if (width < 768) {
        deviceType = 'tablet';
    } else if (width < 992) {
        deviceType = 'laptop';
    } else if (width < 1200) {
        deviceType = 'desktop';
    } else {
        deviceType = 'large-desktop';
    }
    
    // 组装设备信息
    if (mobileDevices.wechat) {
        deviceInfo = '微信浏览器';
    } else if (mobileDevices.weibo) {
        deviceInfo = '微博浏览器';
    } else if (mobileDevices.qq) {
        deviceInfo = 'QQ浏览器';
    } else if (mobileDevices.iphone) {
        deviceInfo = 'iPhone';
    } else if (mobileDevices.ipad) {
        deviceInfo = 'iPad';
    } else if (mobileDevices.android) {
        deviceInfo = 'Android';
    } else {
        deviceInfo = '桌面设备';
    }
    
    // 添加分辨率信息
    deviceInfo += ` (${width}x${height})`;
    
    return {
        type: deviceType,
        isMobile: mobileDevices.mobile,
        isPhone: deviceType === 'phone',
        isTablet: deviceType === 'tablet',
        isDesktop: deviceType === 'desktop' || deviceType === 'laptop' || deviceType === 'large-desktop',
        width: width,
        height: height,
        info: deviceInfo,
        userAgent: ua,
        pixelRatio: window.devicePixelRatio || 1
    };
}

// 应用设备适配样式
function applyDeviceStyles() {
    const device = detectDevice();
    document.body.classList.remove('is-phone', 'is-tablet', 'is-desktop', 'is-mobile', 'is-desktop-device');
    document.body.classList.add('is-' + device.type);
    if (device.isMobile) {
        document.body.classList.add('is-mobile');
    } else {
        document.body.classList.add('is-desktop-device');
    }
    
    const btnContainer = document.querySelector('.text-center.mt-4.mb-4');
    if (btnContainer && device.isPhone) {
        btnContainer.style.padding = '10px 5px';
    }
    
    return device;
}

// 监听窗口大小变化
let resizeTimeout;
window.addEventListener('resize', function() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(function() {
        applyDeviceStyles();
    }, 250);
});

// 全局定时器管理
let tunnelPollInterval = null;
let tunnelRetryInterval = null;
let tunnelStatusInterval = null;

function clearAllPollingIntervals() {
    if (pollingInterval) {
        clearInterval(pollingInterval);
        pollingInterval = null;
    }
    if (tunnelPollInterval) {
        clearInterval(tunnelPollInterval);
        tunnelPollInterval = null;
    }
    if (tunnelRetryInterval) {
        clearInterval(tunnelRetryInterval);
        tunnelRetryInterval = null;
    }
    if (tunnelStatusInterval) {
        clearInterval(tunnelStatusInterval);
        tunnelStatusInterval = null;
    }
}

// 全局函数定义
function showOutputPanel() {
    const panel = document.getElementById('output-panel');
    if (!panel) return;
    panel.style.display = 'block';
    panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function highlightRow(sku, allProductsData) {
    const data = allProductsData || window.allProductsData;
    document.querySelectorAll(`tr[data-sku="${sku}"]`).forEach(row => {
        row.style.background = '#bbdefb';
    });
}

function unhighlightRow(sku, allProductsData) {
    const data = allProductsData || window.allProductsData;
    document.querySelectorAll(`tr[data-sku="${sku}"]`).forEach(row => {
        const priceCell = row.querySelector('td:nth-child(4)');
        if (priceCell) {
            const price = parseFloat((priceCell.textContent || '¥0').replace('¥', '').replace(',', ''));
            const cells = row.querySelectorAll('td');
            const skuCell = cells[1];
            const skuText = skuCell ? skuCell.textContent : '';
            const isAdded = row.classList.contains('added') || (allProductsData && allProductsData.addedProducts && allProductsData.addedProducts.some(ap => ap.货号 === skuText));
            if (price >= 599 && isAdded) row.style.background = '#e8f5e9';
            else if (price >= 599) row.style.background = '#fff3e0';
            else if (isAdded) row.style.background = '#e3f2fd';
            else row.style.background = '';
        } else {
            row.style.background = '';
        }
    });
}

function scrollToSku(sku) {
    const rows = document.querySelectorAll(`tr[data-sku="${sku}"]`);
    if (rows.length > 0) {
        rows[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

function searchProductBySku(sku) {
    if (!sku) return;
    const url = '/api/product/search?sku=' + encodeURIComponent(sku);
    fetch(url)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('搜索失败: ' + data.error);
            return;
        }
        if (data.product) {
            showProductModal(data.product);
        } else {
            alert('未找到该商品');
        }
    })
    .catch(error => {
        console.error('搜索商品出错:', error);
        alert('搜索商品出错: ' + error.message);
    });
}

const DEBUG = true;
const log = DEBUG ? console.log.bind(console, '[调试]') : () => {};
const logError = DEBUG ? console.error.bind(console, '[错误]') : () => {};

function handleVideoError(videoElement, videoUrl, isPreview = false) {
    const url = videoUrl || videoElement.src;
    logError('视频加载失败:', url.substring(0, 50) + '...');
    
    const errorStyle = isPreview 
        ? 'max-width:95%;max-height:90%;background:rgba(255,255,255,0.1);display:flex;align-items:center;justify-content:center;color:white;font-size:16px;text-align:center;padding:20px;border-radius:8px;cursor:pointer;'
        : 'width:150px;height:150px;background:#f5f5f5;display:flex;align-items:center;justify-content:center;color:#999;font-size:12px;text-align:center;padding:5px;border-radius:4px;cursor:pointer;';
    
    const errorContent = isPreview
        ? `<div style="font-size:48px;margin-bottom:10px;">⚠️</div><div>视频加载失败</div><div style="font-size:14px;margin-top:10px;opacity:0.8;">可能是网络问题，点击重试</div>`
        : `视频加载失败<br>点击重试`;
    
    const errorMsg = `<div style="${errorStyle}" onclick="retryVideoLoad(this, '${url.replace(/'/g, "\\'")}', ${isPreview})">${errorContent}</div>`;
    
    if (isPreview) {
        videoElement.outerHTML = errorMsg;
    } else {
        videoElement.parentElement.innerHTML = errorMsg;
    }
}

function retryVideoLoad(errorDiv, videoUrl, isPreview = false) {
    const videoStyle = isPreview
        ? 'max-width:95%;max-height:90%;object-fit:contain;border-radius:8px;cursor:default;background:#000;'
        : 'width:150px;height:150px;object-fit:cover;background:#000;';
    
    const videoPreload = isPreview ? 'auto' : 'metadata';
    const videoAutoplay = isPreview ? 'autoplay' : '';
    const loadingText = isPreview ? '' : '<div class="video-loading" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:white;font-size:12px;">重新加载中...</div>';
    
    const videoHtml = `
        <video id="previewImage" src="${videoUrl}" controls ${videoAutoplay} preload="${videoPreload}" style="${videoStyle}" onclick="event.stopPropagation()" onerror="handleVideoError(this, '${videoUrl.replace(/'/g, "\\'")}', ${isPreview})" onloadeddata="handleVideoLoad(this)">
            您的浏览器不支持视频播放
        </video>
        ${loadingText}
    `;
    
    if (isPreview) {
        const preview = document.getElementById('imagePreview');
        const oldContent = preview?.querySelector('div[style*="max-width:95%"]');
        if (oldContent) {
            oldContent.outerHTML = videoHtml;
        }
    } else {
        errorDiv.parentElement.innerHTML = videoHtml;
    }
}

function handleVideoLoad(videoElement) {
    const loadingDiv = videoElement.parentElement?.querySelector('.video-loading');
    if (loadingDiv) {
        loadingDiv.style.display = 'none';
    }
}

function decodeBase64Url(url) {
    if (!url) return url;
    try {
        if (url.startsWith('http://') || url.startsWith('https://')) {
            log('URL已是HTTP格式:', url.substring(0, 50) + '...');
            return url;
        }
        const decoded = atob(url);
        if (decoded.startsWith('http://') || decoded.startsWith('https://')) {
            log('Base64解码成功:', decoded.substring(0, 50) + '...');
            return decoded;
        }
        log('解码后非HTTP格式，返回原始URL');
        return url;
    } catch (e) {
        logError('Base64解码失败:', e.message);
        return url;
    }
}

function showProductModal(p) {
    const images = p.图片;
    const imageList = images ? (Array.isArray(images) ? images : [images]) : [];
    const validImages = imageList.filter(img => img);
    const decodedImages = validImages.map(img => decodeBase64Url(img));
    
    if (DEBUG && decodedImages.length > 0) {
        log('商品图片数量:', decodedImages.length);
        log('首个URL:', decodedImages[0].substring(0, 50) + '...');
    }
    
    window.currentProductImages = decodedImages;
    window.currentImageIndex = 0;
    
    let modalHtml = `
        <div id="productModal" onclick="if(event.target === this) this.remove()" style="position:fixed;z-index:9999;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);display:flex;align-items:center;justify-content:center;padding:20px;overflow-y:auto;">
            <div style="background:#fff;padding:20px;border-radius:8px;max-width:800px;width:100%;max-height:90vh;overflow-y:auto;position:relative;">
                <button onclick="this.parentElement.parentElement.remove()" style="position:absolute;top:10px;right:15px;font-size:24px;border:none;background:none;cursor:pointer;">&times;</button>
                <h3 style="margin:0 0 15px 0;color:#e4393c;">商品详情</h3>
                <div style="margin-bottom:10px;"><strong>货号:</strong> ${p.货号 || '-'}</div>
                <div style="margin-bottom:10px;"><strong>商品描述:</strong> ${p.商品描述 || '-'}</div>
                <div style="margin-bottom:10px;color:#e4393c;font-size:20px;"><strong>售价:</strong> ${p.售价 || '-'}</div>
                <div style="margin-bottom:10px;color:#2a9838;"><strong>拿货价:</strong> ${p.拿货价 || '-'}</div>
                <div style="margin-bottom:10px;"><strong>员工:</strong> ${p.员工 || '-'}</div>
                <div style="margin-bottom:15px;"><strong>备注:</strong> ${p.备注 || '-'}</div>
    `;
    
    if (validImages.length > 0) {
        modalHtml += `<div style="margin-top:15px;"><strong>图片/视频 (${validImages.length}个):</strong></div>`;
        modalHtml += `<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:10px;justify-content:center;">`;
        
        validImages.forEach((img, i) => {
            const decodedUrl = decodeBase64Url(img);
            const isVideo = decodedUrl.includes('/pvod/') || /\.(mp4|webm|ogg|mov|avi|mkv|flv|wmv|m4v|3gp)(\?|$)/i.test(decodedUrl);
            if (isVideo) {
                modalHtml += `<div style="position:relative;width:150px;height:150px;">
                    <video src="${decodedUrl}" controls preload="metadata" style="width:150px;height:150px;object-fit:cover;background:#000;" onclick="event.stopPropagation()" onerror="handleVideoError(this, '${decodedUrl.replace(/'/g, "\\'")}', false)" onloadeddata="handleVideoLoad(this)">
                        您的浏览器不支持视频播放
                    </video>
                    <div class="video-loading" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:white;font-size:12px;">加载中...</div>
                </div>`;
            } else {
                modalHtml += `<img src="${decodedUrl}" onclick="showImagePreview('${decodedUrl.replace(/'/g, "\\'")}', ${i})" style="width:150px;height:150px;object-fit:cover;border-radius:4px;border:1px solid #ddd;cursor:pointer;" title="点击预览大图" onerror="this.src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUwIiBoZWlnaHQ9IjE1MCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTUwIiBoZWlnaHQ9IjE1MCIgZmlsbD0iI2Y1ZjVmNSIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBkb21pbmFudC1iYXNlbGluZT0ibWlkZGxlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjOTk5IiBmb250LXNpemU9IjE0Ij7nmoTlm77niYHmraLlvTwvdGV4dD48L3N2Zz4='">`;
            }
        });
        modalHtml += `</div>`;
    }
    
    modalHtml += `</div></div>`;
    
    document.body.insertAdjacentHTML('beforeend', modalHtml);
}

function showImagePreview(imageUrl, index) {
    if (typeof index === 'undefined') {
        index = 0;
    }
    window.currentImageIndex = index;
    
    const decodedUrl = decodeBase64Url(imageUrl);
    const isVideo = decodedUrl.includes('/pvod/') || /\.(mp4|webm|ogg|mov|avi|mkv|flv|wmv|m4v|3gp|m4a)(\?|$)/i.test(decodedUrl);
    
    let mediaContent;
    if (isVideo) {
        mediaContent = `<video id="previewImage" src="${decodedUrl}" controls autoplay preload="auto" style="max-width:95%;max-height:90%;object-fit:contain;border-radius:8px;cursor:default;background:#000;" onclick="event.stopPropagation()" onerror="handleVideoError(this, '${decodedUrl.replace(/'/g, "\\'")}', true)">
            您的浏览器不支持视频播放
        </video>`;
    } else {
        mediaContent = `<img id="previewImage" src="${decodedUrl}" style="max-width:95%;max-height:90%;object-fit:contain;border-radius:8px;cursor:default;" onclick="event.stopPropagation()">`;
    }
    
    const previewHtml = `
        <div id="imagePreview" onclick="if(event.target === this) this.remove()" style="position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.95);display:flex;align-items:center;justify-content:center;cursor:zoom-out;overflow:auto;">
            <div style="position:absolute;top:50%;left:0;right:0;transform:translateY(-50%);display:flex;justify-content:space-between;padding:0 10px;pointer-events:none;">
                <button onclick="prevImage()" style="pointer-events:auto;font-size:36px;border:none;background:rgba(255,255,255,0.2);cursor:pointer;color:white;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;">❮</button>
                <button onclick="nextImage()" style="pointer-events:auto;font-size:36px;border:none;background:rgba(255,255,255,0.2);cursor:pointer;color:white;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;">❯</button>
            </div>
            <div style="text-align:center;position:absolute;bottom:20px;left:50%;transform:translateX(-50%);color:white;font-size:14px;background:rgba(0,0,0,0.5);padding:8px 16px;border-radius:20px;">
                <span id="imageCounter">${window.currentImageIndex + 1} / ${window.currentProductImages.length}</span>
            </div>
            ${mediaContent}
            <button onclick="this.parentElement.remove()" style="position:absolute;top:15px;right:20px;font-size:32px;border:none;background:rgba(255,255,255,0.2);cursor:pointer;color:white;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;">&times;</button>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', previewHtml);
    
    const preview = document.getElementById('imagePreview');
    let touchStartX = 0;
    let touchEndX = 0;
    
    preview.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
    }, false);
    
    preview.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    }, false);
    
    function handleSwipe() {
        const swipeThreshold = 50;
        const diff = touchStartX - touchEndX;
        
        if (Math.abs(diff) > swipeThreshold) {
            if (diff > 0) {
                nextImage();
            } else {
                prevImage();
            }
        }
    }
    
    document.addEventListener('keydown', handleKeyDown);
}

function handleKeyDown(e) {
    const preview = document.getElementById('imagePreview');
    if (!preview) {
        document.removeEventListener('keydown', handleKeyDown);
        return;
    }
    
    if (e.key === 'ArrowLeft') {
        prevImage();
        e.preventDefault();
    } else if (e.key === 'ArrowRight') {
        nextImage();
        e.preventDefault();
    } else if (e.key === 'Escape') {
        preview.remove();
        document.removeEventListener('keydown', handleKeyDown);
    }
}

function prevImage() {
    if (!window.currentProductImages || window.currentProductImages.length === 0) return;
    window.currentImageIndex = (window.currentImageIndex - 1 + window.currentProductImages.length) % window.currentProductImages.length;
    updatePreviewImage();
}

function nextImage() {
    if (!window.currentProductImages || window.currentProductImages.length === 0) return;
    window.currentImageIndex = (window.currentImageIndex + 1) % window.currentProductImages.length;
    updatePreviewImage();
}

function updatePreviewImage() {
    const previewImg = document.getElementById('previewImage');
    const counter = document.getElementById('imageCounter');
    if (previewImg && window.currentProductImages && window.currentProductImages.length > 0) {
        const newUrl = window.currentProductImages[window.currentImageIndex];
        const decodedUrl = decodeBase64Url(newUrl);
        const isVideo = decodedUrl.includes('/pvod/') || /\.(mp4|webm|ogg|mov|avi|mkv|flv|wmv|m4v|3gp|m4a)(\?|$)/i.test(decodedUrl);
        
        if (isVideo) {
            const parent = previewImg.parentElement;
            const videoHtml = `<video id="previewImage" src="${decodedUrl}" controls autoplay preload="auto" style="max-width:95%;max-height:90%;object-fit:contain;border-radius:8px;cursor:default;background:#000;" onclick="event.stopPropagation()" onerror="handleVideoError(this, '${decodedUrl.replace(/'/g, "\\'")}', true)">
                您的浏览器不支持视频播放
            </video>`;
            previewImg.outerHTML = videoHtml;
        } else {
            if (previewImg.tagName === 'VIDEO') {
                const parent = previewImg.parentElement;
                const imgHtml = `<img id="previewImage" src="${decodedUrl}" style="max-width:95%;max-height:90%;object-fit:contain;border-radius:8px;cursor:default;" onclick="event.stopPropagation()">`;
                previewImg.outerHTML = imgHtml;
            } else {
                previewImg.src = decodedUrl;
            }
        }
        
        if (counter) {
            counter.textContent = `${window.currentImageIndex + 1} / ${window.currentProductImages.length}`;
        }
    }
}

function showProductDetail(sku) {
    fetch(`/api/product?sku=${encodeURIComponent(sku)}`)
        .then(response => response.json())
        .then(data => {
            if (data.found) {
                const p = data.product;
                showProductModal(p);
            } else {
                alert(data.error || '未找到该商品');
            }
        })
        .catch(error => {
            console.error('查询失败:', error);
            alert('查询失败: ' + error.message);
        });
}

function showProductByDescription(description) {
    fetch(`/api/product/by-description?description=${encodeURIComponent(description)}`)
        .then(response => response.json())
        .then(data => {
            if (data.found) {
                const p = data.product;
                showProductModal(p);
            } else {
                alert(data.error || '未找到该商品');
            }
        })
        .catch(error => {
            console.error('查询失败:', error);
            alert('查询失败: ' + error.message);
        });
}

// 确保DOM加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    const weatherIframe = document.getElementById('weather-iframe');
    if (weatherIframe) {
        const src = weatherIframe.getAttribute('data-src');
        if (src) {
            weatherIframe.src = src;
            weatherIframe.removeAttribute('data-src');
        }
    }

    const device = applyDeviceStyles();
    
    function detectSystem() {
        const userAgent = navigator.userAgent;
        if (userAgent.indexOf('Win') !== -1) return 'Windows';
        if (userAgent.indexOf('Mac') !== -1) return 'Darwin';
        if (userAgent.indexOf('Linux') !== -1) return 'Linux';
        return 'Unknown';
    }
    
    detectSystem();
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
            $('.navbar').addClass('scrolled');
        } else {
            $('.navbar').removeClass('scrolled');
        }
    });
    
    function updateTime() {
    const now = new Date();
    const timeStr = now.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    });
    const timeEl = document.getElementById('current-time');
    if (timeEl) {
        timeEl.innerHTML = '当前时间: ' + timeStr;
    }
}

setInterval(updateTime, 1000);
updateTime();

function copyCommand(cmd) {
    const textarea = document.createElement('textarea');
    textarea.value = cmd;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
}

let pollingInterval = null;
let currentTaskId = null;
let currentChoice = null;
let VENV_PYTHON = 'python';
 const btnIds = {'1': 'btn-run-spider', '4': 'btn-run-cookie', '6': 'btn-run-cleaner'};

function checkCookieStatus() {
    fetch('/api/cookie')
    .then(response => response.json())
    .then(data => {
        const statusEl = document.getElementById('cookie-status');
        let systemInfo = data.system ? ` (${data.system})` : '';
        if (data.error) {
            statusEl.innerHTML = '<i class="fa fa-exclamation-circle" style="color: #f56c6c;"></i> Token有效期: 无效' + systemInfo;
            return;
        }
        
        if (data.expired) {
            statusEl.innerHTML = '<i class="fa fa-times-circle" style="color: #f56c6c;"></i> Token有效期: 已过期' + systemInfo;
            return;
        }
        
        if (data.hours_remaining <= 5) {
            statusEl.innerHTML = '<i class="fa fa-clock-o" style="color: #f56c6c;"></i> Token有效期: ' + data.hours_remaining + '小时' + systemInfo;
        } else {
            let cookieInfo = data.cookie_name ? `(${data.cookie_name}) ` : '';
            statusEl.innerHTML = '<i class="fa fa-check-circle" style="color: #67c23a;"></i> Token有效期: ' + cookieInfo + data.expires + systemInfo;
        }
    })
    .catch(error => {
        const statusEl = document.getElementById('cookie-status');
        statusEl.innerHTML = '<i class="fa fa-exclamation-circle" style="color: #f56c6c;"></i> Token有效期: 获取失败';
    });
}

checkCookieStatus();

function resetButtons() {
    currentTaskId = null;
    currentChoice = null;
    document.querySelectorAll('.btn-run').forEach(b => {
        b.disabled = false;
        b.innerHTML = b.getAttribute('data-original') || b.innerHTML;
    });
    const stopBtn = document.getElementById('btn-stop-task');
    if (stopBtn) stopBtn.style.display = 'none';
}

function runCommand(cmd, btn) {
    if (!btn) return;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> 运行中...';
    
    const outputContent = document.getElementById('output-content');
    
    fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: cmd })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            currentTaskId = data.task_id;
            showOutputPanel();
            if (outputContent) outputContent.innerHTML = '<span style="color: #e6a23c;"><i class="fa fa-spinner fa-spin"></i> 正在执行...</span>';
            pollingInterval = setInterval(() => pollOutput(), 1000);
        } else {
            alert('启动失败: ' + data.error);
            btn.disabled = false;
            btn.innerHTML = '运行';
        }
    })
    .catch(error => {
        console.error('请求失败:', error);
        alert('请求失败: ' + error.message);
        btn.disabled = false;
        btn.innerHTML = '运行';
    });
}

function pollOutput() {
    fetch('/output/' + currentTaskId)
    .then(response => response.json())
    .then(data => {
        const outputDiv = document.getElementById('output-content');
        const statusDiv = document.getElementById('output-status');
        
        if (data.output) {
            const hasComparison = data.output.includes('对比文件:') || data.output.includes('货号对比结果') || data.output.includes('共获取') || data.output.includes('成功获取');
            
            if (!hasComparison && outputDiv) {
                outputDiv.innerHTML = '<pre style="margin: 0; white-space: pre-wrap; word-break: break-all;">' + formatOutput(data.output) + '</pre>';
                const isMobile = window.innerWidth < 576;
                if (!isMobile) {
                    outputDiv.scrollTop = outputDiv.scrollHeight;
                }
            }
            
            if (hasComparison) {
                const spiderContent = document.getElementById('spider-output-content');
                const existingCard = spiderContent ? spiderContent.querySelector('.comparison-card, .products-card') : null;
                if (!existingCard) {
                    showComparisonCard(data.output);
                }
            }
        }
        
        if (data.status === 'completed') {
            clearInterval(pollingInterval);
            const completedChoice = currentChoice;
            console.log('任务完成, choice:', completedChoice);
            if (statusDiv) statusDiv.innerHTML = '<span style="color: #67c23a;">✓ 执行完成 (返回码: ' + data.returncode + ')</span>';
            if (data.returncode === -15) {
                if (statusDiv) statusDiv.innerHTML = '<span style="color: #f56c6c;">■ 已停止运行 (返回码: -15)</span>';
            }
            resetButtons();
            if (completedChoice === 1 || completedChoice === 3) {
                showAllProducts();
            }
        } else if (data.status === 'error') {
            clearInterval(pollingInterval);
            if (statusDiv) statusDiv.innerHTML = '<span style="color: #f56c6c;">✗ 错误: ' + data.error + '</span>';
            resetButtons();
        }
    })
    .catch(error => {
        console.error('pollOutput 出错:', error);
    });
}

function showComparisonCard(output) {
    const spiderPanel = document.getElementById('spider-output-panel');
    const spiderContent = document.getElementById('spider-output-content');
    if (!spiderPanel || !spiderContent) return;
    
    spiderPanel.style.display = 'block';
    spiderPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    
    const lines = output.split('\n');
    let skuData = {};
    let missingSkus = [];
    let inMissingSection = false;
    
    for (let line of lines) {
        line = line.trim();
        
        if (line.includes('货号对比结果')) {
            skuData.type = 'sku';
            inMissingSection = false;
        } else if (line.includes('成功获取') || line.includes('共获取')) {
            skuData.type = 'spider';
            const match = line.match(/(\d+)\s*个/);
            if (match) skuData.totalProducts = match[1];
            inMissingSection = false;
        } else if (line.includes('售价 >=') && line.includes('的商品:')) {
            const match = line.match(/(\d+)\s*个/);
            if (match) skuData.highPriceCount = match[1];
            inMissingSection = false;
        } else if (line.includes('只在JSON中存在但不在Excel中的售价>=599货号数:')) {
            const match = line.match(/:\s*(\d+)/);
            if (match) skuData.highPriceExtraCount = match[1];
            inMissingSection = false;
        } else if (line.includes('只在JSON中存在但不在Excel中的售价>=599的货号:')) {
            skuData.inHighPriceExtraSection = true;
            skuData.highPriceExtraSkus = [];
            inMissingSection = false;
        } else if (skuData.inHighPriceExtraSection && line.match(/^\s*\d+\.\s+\d+\s*$/)) {
            const match = line.match(/\d+\.\s+(\d+)/);
            if (match) skuData.highPriceExtraSkus.push(match[1]);
        } else if (line.includes('预计售出价格累计:')) {
            const match = line.match(/¥[\d,.]+/);
            if (match) skuData.totalPrice = match[0];
            inMissingSection = false;
        } else if (line.includes('【新增商品】')) {
            skuData.inAddedSection = true;
            skuData.addedProducts = [];
            inMissingSection = false;
        } else if (line.includes('【删除商品】')) {
            skuData.inAddedSection = false;
            skuData.inDeletedSection = true;
            skuData.deletedProducts = [];
            inMissingSection = false;
        } else if ((skuData.inAddedSection || skuData.inDeletedSection) && line.includes('"货号":')) {
            const skuMatch = line.match(/"货号":\s*"([^"]+)"/);
            const nameMatch = line.match(/"商品描述":\s*"([^"]+)"/);
            const priceMatch = line.match(/"售价":\s*"([^"]+)"/);
            
            const product = {
                sku: skuMatch ? skuMatch[1] : '',
                name: nameMatch ? nameMatch[1] : '',
                price: priceMatch ? priceMatch[1] : ''
            };
            
            if (skuData.inAddedSection && product.sku) {
                skuData.addedProducts.push(product);
            } else if (skuData.inDeletedSection && product.sku) {
                skuData.deletedProducts.push(product);
            }
        } else if (line.includes('平均每个设备售出均价:')) {
            const match = line.match(/¥[\d,.]+/);
            if (match) skuData.avgPrice = match[0];
            inMissingSection = false;
        } else if (line.includes('闲鱼平台手续费累计:')) {
            const match = line.match(/¥[\d,.]+/);
            if (match) skuData.fee = match[0];
            inMissingSection = false;
        } else if (line.includes('输入货号总数:')) {
            const match = line.match(/(\d+)$/);
            if (match) skuData.inputCount = match[1];
            inMissingSection = false;
        } else if (line.includes('JSON中货号总数:')) {
            const match = line.match(/(\d+)$/);
            if (match) skuData.jsonCount = match[1];
            inMissingSection = false;
        } else if (line.includes('已存在货号数:')) {
            const match = line.match(/(\d+)$/);
            if (match) skuData.existCount = match[1];
            inMissingSection = false;
        } else if (line.includes('缺失货号数:')) {
            const match = line.match(/(\d+)$/);
            if (match) skuData.missingCount = match[1];
            inMissingSection = false;
        } else if (line.includes('JSON中多余货号数:')) {
            const match = line.match(/(\d+)$/);
            if (match) skuData.extraCount = match[1];
            inMissingSection = false;
        } else if (line.includes('重复序列号数:')) {
            const match = line.match(/(\d+)$/);
            if (match) skuData.duplicateCount = match[1];
            inMissingSection = false;
        } else if (line.includes('对比文件:')) {
             skuData.type = 'product';
             inMissingSection = false;
         } else if (line.includes('新增商品数:')) {
             skuData.newProducts = line.split(':')[1].trim();
             inMissingSection = false;
         } else if (line.includes('删除商品数:')) {
             skuData.deletedProducts = line.split(':')[1].trim();
             inMissingSection = false;
         } else if (line.includes('新增高价商品数:')) {
             skuData.newHighPrice = line.split(':')[1].trim();
             inMissingSection = false;
         } else if (line.includes('预计售出价格累计:')) {
             const match = line.match(/¥[\d,.]+/);
             if (match) skuData.totalPrice = match[0];
             inMissingSection = false;
         } else if (line.includes('缺失货号列表:') || line.includes('缺失的货号:')) {
            inMissingSection = true;
            continue;
        } else if (inMissingSection && line.match(/^\s*\d+\.\s+\d+\s*$/)) {
            const match = line.match(/\d+\.\s+(\d+)/);
            if (match) missingSkus.push(match[1]);
        }
    }
    
    missingSkus = [...new Set(missingSkus)];
     
     const displayCount = parseInt(skuData.missingCount) || missingSkus.length;
     missingSkus = missingSkus.slice(0, displayCount);
    
    const existingCard = spiderContent.querySelector('.comparison-card');
    if (existingCard) existingCard.remove();
    
    if (skuData.type === 'sku') {
        let cardHtml = `
        <div class="comparison-card">
            <div class="comparison-header" style="background: #E6A23C;">
                <i class="fa fa-barcode"></i> 货号对比结果
            </div>
            <div class="comparison-body">
                <div class="comparison-stats">
                    <div class="stat-item ${skuData.inputCount > 0 ? 'stat-info' : ''}">
                        <span class="stat-value">${skuData.inputCount || 0}</span>
                        <span class="stat-label">输入货号</span>
                    </div>
                    <div class="stat-item ${skuData.jsonCount > 0 ? 'stat-info' : ''}">
                        <span class="stat-value">${skuData.jsonCount || 0}</span>
                        <span class="stat-label">JSON货号</span>
                    </div>
                    <div class="stat-item ${skuData.existCount > 0 ? 'stat-success' : ''}">
                        <span class="stat-value">${skuData.existCount || 0}</span>
                        <span class="stat-label">已存在</span>
                    </div>
                    <div class="stat-item ${skuData.missingCount > 0 ? 'stat-danger' : ''}">
                        <span class="stat-value">${skuData.missingCount || 0}</span>
                        <span class="stat-label">缺失货号</span>
                    </div>
                </div>
                <div class="comparison-stats">
                    <div class="stat-item ${skuData.extraCount > 0 ? 'stat-warning' : ''}">
                        <span class="stat-value">${skuData.extraCount || 0}</span>
                        <span class="stat-label">JSON多余</span>
                    </div>
                    <div class="stat-item ${skuData.duplicateCount > 0 ? 'stat-warning' : ''}">
                        <span class="stat-value">${skuData.duplicateCount || 0}</span>
                        <span class="stat-label">重复序列号</span>
                    </div>
                    <div class="stat-item ${skuData.highPriceExtraCount > 0 ? 'stat-danger' : ''}">
                        <span class="stat-value">${skuData.highPriceExtraCount || 0}</span>
                        <span class="stat-label">高价多余(≥599)</span>
                    </div>
                </div>
        `;
        
        if (missingSkus.length > 0) {
            const items = missingSkus.map(sku => `<span class="sku-tag">${sku}</span>`).join('');
            cardHtml += `
                <div class="missing-skus">
                    <div class="missing-title">缺失货号列表:</div>
                    <div class="sku-container">${items}</div>
                </div>
            `;
        }
        
        if (skuData.highPriceExtraSkus && skuData.highPriceExtraSkus.length > 0) {
            const items = skuData.highPriceExtraSkus.map(sku => `<span class="sku-tag" onclick="showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
            cardHtml += `
                <div class="missing-skus" style="background: #fff3e0; border-color: #ffcc80;">
                    <div class="missing-title" style="color: #E6A23C;">高价多余货号列表(≥599且不在Excel):</div>
                    <div class="sku-container">${items}</div>
                </div>
            `;
        }
        
        cardHtml += `</div></div>`;
        spiderContent.insertAdjacentHTML('beforeend', cardHtml);
        
    } else if (skuData.newProducts !== undefined || skuData.deletedProducts !== undefined) {
        let cardHtml = `
        <div class="comparison-card">
            <div class="comparison-header">
                <i class="fa fa-exchange"></i> 商品对比结果
            </div>
            <div class="comparison-body">
                <div class="comparison-row">
                    <span class="comparison-label">对比文件:</span>
                    <span class="comparison-value">${skuData.oldFile || ''} → ${skuData.newFile || ''}</span>
                </div>
                <div class="comparison-stats">
                    <div class="stat-item ${skuData.newProducts > 0 ? 'stat-success' : ''}">
                        <span class="stat-value">${skuData.newProducts || 0}</span>
                        <span class="stat-label">新增商品</span>
                    </div>
                    <div class="stat-item ${skuData.deletedProducts > 0 ? 'stat-danger' : ''}">
                        <span class="stat-value">${skuData.deletedProducts || 0}</span>
                        <span class="stat-label">删除商品</span>
                    </div>
                    <div class="stat-item ${skuData.newHighPrice > 0 ? 'stat-warning' : ''}">
                        <span class="stat-value">${skuData.newHighPrice || 0}</span>
                        <span class="stat-label">新增高价</span>
                    </div>
                </div>
        `;
        
        if (skuData.totalPrice) {
            cardHtml += `
                <div class="comparison-summary">
                    <span class="summary-label">预计售出总价:</span>
                    <span class="summary-value">${skuData.totalPrice}</span>
                </div>
            `;
        }
        
        cardHtml += `</div></div>`;
        spiderContent.insertAdjacentHTML('beforeend', cardHtml);
        
    } else if (skuData.type === 'spider' && skuData.totalProducts) {
        let cardHtml = `
        <div class="comparison-card">
            <div class="comparison-header" style="background: #67c23a;">
                <i class="fa fa-spider"></i> 爬虫执行结果
            </div>
            <div class="comparison-body">
                <div class="comparison-stats">
                    <div class="stat-item stat-info">
                        <span class="stat-value">${skuData.totalProducts || 0}</span>
                        <span class="stat-label">总商品数</span>
                    </div>
                    <div class="stat-item ${skuData.highPriceCount > 0 ? 'stat-warning' : ''}">
                        <span class="stat-value">${skuData.highPriceCount || 0}</span>
                        <span class="stat-label">高价商品(≥599)</span>
                    </div>
                </div>
                <div class="comparison-stats">
                    <div class="stat-item">
                        <span class="stat-value" style="color: #E6A23C; font-weight: bold;">${skuData.totalPrice || '-'}</span>
                        <span class="stat-label">预计售出总价</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">${skuData.avgPrice || '-'}</span>
                        <span class="stat-label">平均售出均价</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value" style="color: #f56c6c;">${skuData.fee || '-'}</span>
                        <span class="stat-label">平台手续费</span>
                    </div>
                </div>
        `;
        
        if (skuData.addedProducts && skuData.addedProducts.length > 0) {
            cardHtml += `
                <div class="change-section">
                    <div class="change-title" style="color: #67c23a;">新增商品序列号 (${skuData.addedProducts.length}个)</div>
                    <div class="change-table-container">
                        <table class="change-table">
                            <thead><tr><th>序号</th><th>货号</th><th>售价</th></tr></thead>
                            <tbody>
                                ${skuData.addedProducts.map((p, idx) => `<tr>
                                    <td>${idx + 1}</td>
                                    <td><a href="javascript:void(0)" onclick="showProductDetail('${p.sku}')" style="color: #409EFF; text-decoration: none;">${p.sku}</a></td>
                                    <td>${p.price || '-'}</td>
                                </tr>`).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }
        
        if (skuData.deletedProducts && skuData.deletedProducts.length > 0) {
            cardHtml += `
                <div class="change-section">
                    <div class="change-title" style="color: #f56c6c;">删除商品序列号 (${skuData.deletedProducts.length}个)</div>
                    <div class="change-table-container">
                        <table class="change-table">
                            <thead><tr><th>序号</th><th>货号</th><th>售价</th></tr></thead>
                            <tbody>
                                ${skuData.deletedProducts.map((p, idx) => `<tr>
                                    <td>${idx + 1}</td>
                                    <td>${p.sku}</td>
                                    <td>${p.price || '-'}</td>
                                </tr>`).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }
        
        if (skuData.newHighPriceProducts && skuData.newHighPriceProducts.length > 0) {
            cardHtml += `
                <div class="change-section">
                    <div class="change-title" style="color: #409EFF;">新增高价商品(≥599) (${skuData.newHighPriceProducts.length}个)</div>
                    <div class="change-table-container">
                        <table class="change-table">
                            <thead><tr><th>序号</th><th>货号</th><th>售价</th></tr></thead>
                            <tbody>
                                ${skuData.newHighPriceProducts.map((p, idx) => `<tr>
                                    <td>${idx + 1}</td>
                                    <td><a href="javascript:void(0)" onclick="console.log('[按钮点击] 查看商品详情:', '${p.sku}'); showProductDetail('${p.sku}')" style="color: #409EFF; text-decoration: none;">${p.sku}</a></td>
                                    <td>${p.price || '-'}</td>
                                </tr>`).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }
        
        cardHtml += `</div></div>`;
        spiderContent.insertAdjacentHTML('beforeend', cardHtml);
        
        const isMobile = window.innerWidth < 576;
        if (isMobile) {
            const spiderOutputContent = document.getElementById('spider-output-content');
            if (spiderOutputContent) {
                spiderOutputContent.scrollTop = 0;
            }
        }
    }
}

function showAllProducts() {
    const productsPanel = document.getElementById('products-panel');
    const productsContent = document.getElementById('products-content');
    if (!productsPanel || !productsContent) {
        alert('找不到商品面板');
        return;
    }
    
    const timestamp = new Date().getTime();
    fetch(`/api/products?t=${timestamp}`, {
        method: 'GET',
        cache: 'no-cache',
        headers: {
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        
        productsPanel.style.display = 'block';
        productsPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
        
        const existingCard = productsContent.querySelector('.products-card, .comparison-card');
        if (existingCard) existingCard.remove();
        
        window.allProductsData = data;
        console.log('商品数据加载成功, 总数:', data.total);
        
        function renderTable(products, title, color, tableId) {
            if (!products || products.length === 0) return '';
            let tableHtml = `
                <div class="change-section">
                    <div class="change-title" style="color: ${color};">${title}</div>
                    <div class="change-table-container">
                        <table class="change-table" id="${tableId}">
                            <thead><tr><th>序号</th><th>货号</th><th>商品描述</th><th>售价</th><th>员工</th></tr></thead>
                            <tbody>
            `;
            products.forEach((p, i) => {
                const sku = p.货号 || '';
                const desc = p.商品描述 || '';
                const isHighPrice = parseFloat((p.售价 || '¥0').replace('¥', '').replace(',', '')) >= 599;
                const isAdded = data.addedProducts && data.addedProducts.some(ap => ap.货号 === sku);
                let rowStyle = '';
                if (isHighPrice && isAdded) rowStyle = 'background: #e8f5e9;';
                else if (isHighPrice) rowStyle = 'background: #fff3e0;';
                else if (isAdded) rowStyle = 'background: #e3f2fd;';
                const descDisplay = desc.length > 20 ? desc.substring(0, 20) + '...' : desc;
                tableHtml += `<tr data-sku="${sku}" style="${rowStyle}" onmouseover="highlightRow('${sku}')" onmouseout="unhighlightRow('${sku}')">
                    <td>${i + 1}</td>
                    <td><a href="javascript:void(0)" onclick="console.log('[按钮点击] 高亮并定位货号:', '${sku}'); highlightRow('${sku}'); scrollToSku('${sku}'); searchProductBySku('${sku}')">${sku || '-'}</a></td>
                    <td><a href="javascript:void(0)" onclick="console.log('[按钮点击] 查看商品详情:', '${desc.replace(/'/g, "\\'")}'); showProductByDescription('${desc.replace(/'/g, "\\'")}')" style="color: #409EFF; text-decoration: none; cursor: pointer;" title="点击查看详情">${descDisplay}</a></td>
                    <td style="font-weight: bold;">${p.售价 || '-'}</td>
                    <td>${p.员工 || '-'}</td>
                </tr>`;
            });
            tableHtml += `</tbody></table></div></div>`;
            return tableHtml;
        }
        
        let html = `
        <div class="comparison-card products-card">
            <div class="comparison-header" style="background: #409EFF;">
                <i class="fa fa-list"></i> 商品数据汇总 - ${data.filename}
            </div>
            <div class="comparison-body">
                <div class="comparison-stats">
                    <div class="stat-item">
                        <span class="stat-value" style="color: #E6A23C; font-weight: bold;">${data.totalPrice || '-'}</span>
                        <span class="stat-label">预计售出总价</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value">${data.avgPrice || '-'}</span>
                        <span class="stat-label">平均售出均价</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-value" style="color: #f56c6c;">${data.fee || '-'}</span>
                        <span class="stat-label">平台手续费</span>
                    </div>
                </div>
                <div class="summary-stats">
                    <span class="summary-badge" style="background: #409EFF;">总商品: ${data.total}个</span>
                    <span class="summary-badge" style="background: #E6A23C;">高价(≥599): ${data.highPriceCount || 0}个</span>
                    <span class="summary-badge" style="background: #67c23a;">新增: ${data.addedCount || 0}个</span>
                    <span class="summary-badge" style="background: #e8f5e9; color: #2e7d32;">↔ 高价+新增</span>
                </div>
                ${renderTable(data.products, '总商品列表 (' + data.total + '个)', '#409EFF', 'table-all')}
                ${renderTable(data.highPriceProducts, '高价商品 (≥599元, ' + (data.highPriceCount || 0) + '个)', '#E6A23C', 'table-highprice')}
                ${renderTable(data.highPriceNewProducts, '高价新增 (≥599元且不在之前Excel, ' + (data.highPriceNewCount || 0) + '个)', '#f56c6c', 'table-highprice-new')}
                ${renderTable(data.addedProducts, '新增商品 (' + (data.addedCount || 0) + '个)', '#67c23a', 'table-added')}
            </div>
        </div>`;
        productsContent.insertAdjacentHTML('beforeend', html);
        
        // 添加表格滚动联动功能
        setTimeout(() => {
            const tableContainers = productsContent.querySelectorAll('.change-table-container');
            let isScrolling = false;
            
            // 统一的滚动同步函数
            function syncScroll(sourceContainer, sourceIndex) {
                if (isScrolling) return;
                isScrolling = true;
                
                const scrollTop = sourceContainer.scrollTop;
                const scrollLeft = sourceContainer.scrollLeft;
                
                tableContainers.forEach((otherContainer, otherIndex) => {
                    if (otherIndex !== sourceIndex) {
                        otherContainer.scrollTop = scrollTop;
                        otherContainer.scrollLeft = scrollLeft;
                    }
                });
                
                setTimeout(() => { isScrolling = false; }, 10);
            }
            
            // 为每个表格容器添加滚动事件（桌面端）
            tableContainers.forEach((container, index) => {
                container.addEventListener('scroll', function(e) {
                    syncScroll(e.target, index);
                });
                
                // 移动端触摸滚动支持
                let touchStartY = 0;
                let touchStartX = 0;
                
                container.addEventListener('touchstart', function(e) {
                    touchStartY = e.touches[0].clientY;
                    touchStartX = e.touches[0].clientX;
                }, { passive: true });
                
                container.addEventListener('touchmove', function(e) {
                    syncScroll(e.target, index);
                }, { passive: true });
            });
            
            const isMobile = window.innerWidth < 576;
            if (!isMobile) {
                productsContent.scrollTop = productsContent.scrollHeight;
            }
        }, 100);
    })
    .catch(error => {
        console.error('获取商品失败:', error);
         alert('获取商品失败: ' + error.message + '\n详情请查看控制台');
    });
}

function runFunction(choice) {
   currentChoice = choice;
    const btnId = btnIds[choice];
    const btn = document.getElementById(btnId);
    if (!btn) {
        console.error('找不到按钮:', choice, 'btnId:', btnId);
        alert('找不到按钮: ' + choice);
        return;
    }
    btn.setAttribute('data-original', btn.innerHTML);
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> 运行中...';
    
    document.querySelectorAll('.btn-run').forEach(b => {
        if (b.id !== btnIds[choice]) {
            b.disabled = true;
        }
    });
    
    const stopBtn = document.getElementById('btn-stop-task');
    if (stopBtn) stopBtn.style.display = 'inline-block';
    
    const cmd = VENV_PYTHON + ' main.py --task ' + choice;
    
    fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: cmd })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            currentTaskId = data.task_id;
            showOutputPanel();
            const outputContent = document.getElementById('output-content');
            if (outputContent) outputContent.innerHTML = '<span style="color: #e6a23c;"><i class="fa fa-spinner fa-spin"></i> 正在执行...</span>';
            pollingInterval = setInterval(() => pollOutput(), 1000);
        } else {
            alert('启动失败: ' + data.error);
            btn.disabled = false;
            btn.innerHTML = btn.getAttribute('data-original');
        }
    })
    .catch(error => {
        alert('请求失败: ' + error.message);
        btn.disabled = false;
        btn.innerHTML = btn.getAttribute('data-original');
    });
}

function sendUserInput() {
    const inputEl = document.getElementById('user-input');
    if (!inputEl) return;
    const input = inputEl.value;
    if (!input) return;
    if (!currentTaskId) {
        alert('没有正在运行的任务');
        return;
    }
    
    fetch('/input', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task_id: currentTaskId, input: input })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const userInput = document.getElementById('user-input');
            if (userInput) userInput.value = '';
        } else {
            alert('发送失败: ' + data.error);
        }
    })
    .catch(error => {
        alert('请求失败: ' + error.message);
    });
}

function stopTask() {
    if (!currentTaskId) {
        alert('没有正在运行的任务');
        return;
    }
    
    fetch('/kill', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task_id: currentTaskId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            clearInterval(pollingInterval);
            const statusEl = document.getElementById('output-status');
            if (statusEl) statusEl.innerHTML = '<span style="color: #f56c6c;">■ 已停止运行</span>';
            const inputArea = document.getElementById('output-input-area');
            if (inputArea) inputArea.style.display = 'none';
            resetButtons();
        } else {
            alert('停止失败: ' + (data.error || '未知错误'));
        }
    })
    .catch(error => {
        alert('请求失败: ' + error.message);
    });
}

const userInputEl = document.getElementById('user-input');
if (userInputEl) {
    userInputEl.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendUserInput();
        }
    });
}

// 统一按钮事件绑定
document.querySelectorAll('.btn-run').forEach(function(btn) {
    btn.onclick = function() {
        var choice = this.getAttribute('data-func');
        var btnId = this.id || 'unknown';
        console.log('[按钮点击] id:', btnId, 'data-func:', choice);
        if (choice && choice != '6') {
            runFunction(parseInt(choice));
        } else if (choice == '6') {
            console.log('[功能6] 打开文件清理面板');
            showCleanerPanel();
        }
    };
});

const viewProductsBtn = document.getElementById('btn-view-products');
if (viewProductsBtn) {
    viewProductsBtn.onclick = function() {
        console.log('[按钮点击] 查看所有商品');
        showAllProducts();
    };
}

const tunnelBtn = document.getElementById('btn-run-tunnel');
if (tunnelBtn) {
    tunnelBtn.onclick = function() {
        console.log('[按钮点击] 隧道共享');
        startTunnelAndShow();
    };
}

// 一键启动隧道并显示结果
async function startTunnelAndShow() {
    const btn = document.getElementById('btn-run-tunnel');
    if (!btn) return;
    btn.disabled = true;
    btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> 启动中...';

    try {
        const serverRes = await fetch('/api/server/info');
        const serverData = await serverRes.json();

        const startRes = await fetch('/api/tunnel/start', { method: 'POST' });
        const startData = await startRes.json();

        const localUrl = serverData.success ? serverData.local_url : 'http://127.0.0.1:8888';
        const lanUrl = serverData.success && serverData.lan_url ? serverData.lan_url : '';

        const tunnelPanel = document.getElementById('tunnel-panel');
        const tunnelContent = document.getElementById('tunnel-content');
        if (!tunnelPanel || !tunnelContent) {
            alert('找不到隧道面板');
            btn.disabled = false;
            btn.innerHTML = '<i class="fa fa-external-link"></i> 7. 隧道共享';
            return;
        }
        
        tunnelPanel.style.display = 'block';
        tunnelPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
        tunnelContent.innerHTML = `
            <div class="card mt-3">
                <div class="card-header bg-success text-white">
                    <h5 class="mb-0"><i class="fa fa-check-circle"></i> 隧道已启动</h5>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label><strong><i class="fa fa-desktop"></i> 本地地址:</strong></label>
                        <div class="p-2 bg-light rounded">
                            <code>${localUrl}</code>
                        </div>
                    </div>
                    ${lanUrl ? `
                    <div class="form-group">
                        <label><strong><i class="fa fa-wifi"></i> 局域网地址:</strong></label>
                        <div class="p-2 bg-light rounded">
                            <code>${lanUrl}</code>
                            <small class="text-muted d-block">同一网络下的设备可访问</small>
                        </div>
                    </div>
                    ` : ''}
                    <div class="form-group">
                        <label><strong><i class="fa fa-globe"></i> 公网地址:</strong></label>
                        <div class="p-2 bg-success text-white rounded" id="tunnel-public-url-container">
                            <i class="fa fa-spinner fa-spin"></i> <span id="tunnel-public-url">获取中...</span>
                        </div>
                    </div>
                    <div class="text-center mt-3">
                        <button class="btn btn-info btn-lg" onclick="showTunnelSection()">
                            <i class="fa fa-cog"></i> 管理隧道
                        </button>
                    </div>

                </div>
            </div>
        `;

        let retryCount = 0;
        const maxRetries = 120;
        tunnelPollInterval = setInterval(async () => {
            retryCount++;
            try {
                const statusRes = await fetch('/api/tunnel/status');
                const statusData = await statusRes.json();

                if (statusData.url && statusData.url.startsWith('http')) {
                    clearInterval(tunnelPollInterval);
                    tunnelPollInterval = null;
                    const urlContainer = document.getElementById('tunnel-public-url-container');
                    if (urlContainer) {
                        urlContainer.className = 'p-2 bg-success text-white rounded';
                        urlContainer.innerHTML = `
                            <i class="fa fa-check-circle"></i>
                            <a href="${statusData.url}" target="_blank" class="text-white font-weight-bold" style="word-break: break-all;">
                                <i class="fa fa-external-link"></i> ${statusData.url}
                            </a>
                            <button class="btn btn-sm btn-light ml-2 btn-copy-tunnel-url" id="btn-copy-tunnel-url" data-url="${statusData.url}">
                                <i class="fa fa-copy"></i> 复制
                            </button>
                        `;
                        const newCopyBtn = document.getElementById('btn-copy-tunnel-url');
                        if (newCopyBtn) {
                            newCopyBtn.onclick = function() {
                                console.log('[按钮点击] 复制隧道URL:', this.dataset.url);
                                copyToClipboard(this.dataset.url);
                                this.innerHTML = '<i class="fa fa-check"></i> 已复制';
                                setTimeout(() => {
                                    this.innerHTML = '<i class="fa fa-copy"></i> 复制';
                                }, 2000);
                            };
                        }
                    }
                } else if (retryCount >= maxRetries) {
                    console.log('[隧道共享] 达到最大重试次数，停止轮询');
                    clearInterval(tunnelPollInterval);
                    tunnelPollInterval = null;
                    const pubUrl = document.getElementById('tunnel-public-url');
                    if (pubUrl) pubUrl.textContent = '获取失败，请检查网络连接';
                }
            } catch (e) {
                console.error('[隧道共享] 获取状态失败:', e);
            }
        }, 1000);

        if (!startData.success) {
            console.log('[隧道共享] 启动失败:', startData.error);
            const alertDiv = document.createElement('div');
            alertDiv.className = 'alert alert-danger mt-3';
            alertDiv.innerHTML = '<i class="fa fa-exclamation-triangle"></i> <strong>启动失败:</strong> ' + (startData.error || '未知错误');
            if (tunnelContent) tunnelContent.insertBefore(alertDiv, tunnelContent.firstChild);
        }

    } catch (e) {
        console.error('[隧道共享] 操作失败:', e);
        alert('操作失败: ' + e.message);
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa fa-external-link"></i> 7. 隧道共享';
        }
    }
}

function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function() {
            showToast('链接已复制到剪贴板');
        }, function() {
            fallbackCopy(text);
        });
    } else {
        fallbackCopy(text);
    }
}

function fallbackCopy(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    try {
        document.execCommand('copy');
        showToast('链接已复制到剪贴板');
    } catch (err) {
        alert('复制失败，请手动复制');
    }
    document.body.removeChild(textarea);
}

function showToast(message) {
    const existing = document.getElementById('copy-toast');
    if (existing) existing.remove();
    const toast = document.createElement('div');
    toast.id = 'copy-toast';
    toast.style.cssText = 'position:fixed;top:20px;left:50%;transform:translateX(-50%);background:#28a745;color:#fff;padding:10px 20px;border-radius:5px;z-index:9999;font-size:14px;';
    toast.innerHTML = '<i class="fa fa-check"></i> ' + message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}

// 绑定货号对比API按钮
document.querySelectorAll('.btn-sku-api').forEach(function(btn) {
    btn.onclick = function() {
        var apiUrl = this.getAttribute('data-api');
        var btnId = this.id || 'unknown';
        console.log('[按钮点击] id:', btnId, 'api:', apiUrl);
        
        if (apiUrl === '/api/sku/compare/txt') {
            console.log('[功能] 货号文本对比 - 显示输入面板');
            showSkuInputPanel();
            return;
        }
        
        if (apiUrl) {
            console.log('[功能] 调用对比API:', apiUrl);
            fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert('对比失败: ' + data.error);
                    return;
                }
                
                showOutputPanel();
                const outputPanel = document.getElementById('output-panel');
                const existingCard = outputPanel.querySelector('.comparison-card, .products-card');
                if (existingCard) existingCard.remove();
                
                let cardHtml = `
                <div class="comparison-card">
                    <div class="comparison-header" style="background: #E6A23C;">
                        <i class="fa fa-barcode"></i> 货号对比结果
                    </div>
                    <div class="comparison-body">
                        <div class="comparison-stats">
                            <div class="stat-item ${data.txt_count > 0 ? 'stat-info' : ''}">
                                <span class="stat-value">${data.txt_count || 0}</span>
                                <span class="stat-label">输入货号</span>
                            </div>
                            <div class="stat-item ${data.extra_count > 0 ? 'stat-warning' : ''}">
                                <span class="stat-value">${data.extra_count || 0}</span>
                                <span class="stat-label">JSON多余</span>
                            </div>
                            <div class="stat-item ${data.json_count > 0 ? 'stat-info' : ''}">
                                <span class="stat-value">${data.json_count || 0}</span>
                                <span class="stat-label">JSON货号</span>
                            </div>
                            <div class="stat-item ${data.common_count > 0 ? 'stat-success' : ''}">
                                <span class="stat-value">${data.common_count || 0}</span>
                                <span class="stat-label">已存在</span>
                            </div>
                        </div>
                        <div class="comparison-stats">
                            <div class="stat-item ${data.missing_count > 0 ? 'stat-danger' : ''}">
                                <span class="stat-value">${data.missing_count || 0}</span>
                                <span class="stat-label">缺失货号</span>
                            </div>
                            <div class="stat-item ${data.duplicate_count > 0 ? 'stat-warning' : ''}">
                                <span class="stat-value">${data.duplicate_count || 0}</span>
                                <span class="stat-label">重复序列号</span>
                            </div>
                            <div class="stat-item ${data.high_price_count > 0 ? 'stat-success' : ''}">
                                <span class="stat-value">${data.high_price_count || 0}</span>
                                <span class="stat-label">高价商品(≥599)</span>
                            </div>
                        </div>
                        <div class="comparison-stats">
                            <div class="stat-item ${data.added_products_count > 0 ? 'stat-success' : ''}">
                                <span class="stat-value">${data.added_products_count || 0}</span>
                                <span class="stat-label">新增商品</span>
                            </div>
                            <div class="stat-item ${data.removed_products_count > 0 ? 'stat-danger' : ''}">
                                <span class="stat-value">${data.removed_products_count || 0}</span>
                                <span class="stat-label">删除商品</span>
                            </div>
                            <div class="stat-item ${data.added_high_price_count > 0 ? 'stat-info' : ''}">
                                <span class="stat-value">${data.added_high_price_count || 0}</span>
                                <span class="stat-label">新增高价(≥599)</span>
                            </div>
                        </div>
                `;
                
                if ((data.duplicates && Object.keys(data.duplicates).length > 0) || (data.duplicates_excel && Object.keys(data.duplicates_excel).length > 0)) {
                    const dupData = data.duplicates || data.duplicates_excel || {};
                    const dupItems = Object.entries(dupData).map(([sku, count]) => `<span class="sku-tag" style="background: #ff9800; color: white;">${sku} (重复${count}次)</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #fff3e0; border-color: #ff9800;">
                            <div class="missing-title" style="color: #e65100;">Excel重复货号列表:</div>
                            <div class="sku-container">${dupItems}</div>
                        </div>
                    `;
                }
                
                if (data.duplicates_json && Object.keys(data.duplicates_json).length > 0) {
                    const dupItems = Object.entries(data.duplicates_json).map(([sku, count]) => `<span class="sku-tag" style="background: #e91e63; color: white;">${sku} (重复${count}次)</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #fce4ec; border-color: #e91e63;">
                            <div class="missing-title" style="color: #c2185b;">JSON重复货号列表:</div>
                            <div class="sku-container">${dupItems}</div>
                        </div>
                    `;
                }
                
                if (data.added_products && data.added_products.length > 0) {
                    const items = data.added_products.map(sku => `<span class="sku-tag" onclick="showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #e8f5e9; border-color: #81c784;">
                            <div class="missing-title" style="color: #2e7d32;">新增商品 (${data.added_products_count}个):</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                if (data.added_high_price && data.added_high_price.length > 0) {
                    const items = data.added_high_price.map(sku => `<span class="sku-tag" onclick="showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #e3f2fd; border-color: #64b5f6;">
                            <div class="missing-title" style="color: #1976d2;">新增高价商品(≥599) (${data.added_high_price_count}个):</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                if (data.removed_products && data.removed_products.length > 0) {
                    const items = data.removed_products.map(sku => `<span class="sku-tag">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #ffebee; border-color: #ef5350;">
                            <div class="missing-title" style="color: #c62828;">删除的商品 (${data.removed_products_count}个):</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                if (data.missing_in_json && data.missing_in_json.length > 0) {
                    const items = data.missing_in_json.map(sku => `<span class="sku-tag">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus">
                            <div class="missing-title">缺失货号列表:</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                if (data.extra_in_json && data.extra_in_json.length > 0) {
                    const items = data.extra_in_json.map(sku => `<span class="sku-tag" onclick="console.log('[按钮点击] 查看商品详情:', '${sku}'); showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #fff3e0; border-color: #ffb74d;">
                            <div class="missing-title" style="color: #f57c00;">JSON多余货号(所有价格):</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                if (data.high_price_extra_in_json && data.high_price_extra_in_json.length > 0) {
                    const items = data.high_price_extra_in_json.map(sku => `<span class="sku-tag" onclick="console.log('[按钮点击] 查看商品详情:', '${sku}'); showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #ffebee; border-color: #ef9a9a;">
                            <div class="missing-title" style="color: #c62828;">JSON多余货号(高价商品≥599):</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                if (data.high_price_existing && data.high_price_existing.length > 0) {
                    const items = data.high_price_existing.map(sku => `<span class="sku-tag" onclick="showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
                    cardHtml += `
                        <div class="missing-skus" style="background: #e8f5e9; border-color: #81c784;">
                            <div class="missing-title" style="color: #388e3c;">高价商品中已存在于Excel的货号:</div>
                            <div class="sku-container">${items}</div>
                        </div>
                    `;
                }
                
                cardHtml += `</div></div>`;
                
                outputPanel.insertAdjacentHTML('beforeend', cardHtml);
            })
            .catch(error => {
                alert('请求失败: ' + error.message);
            });
        }
    };
});

});

// 全局函数定义
function formatOutput(text) {
    if (!text) return '';
    
    text = text.replace(/\x1b\[[0-9;]*m/g, '');
    text = text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    
    let lines = text.split('\n');
    let filteredLines = [];
    let inCookieSection = false;
    
    for (let line of lines) {
        if (line.includes('验证Cookie状态') || line.includes('Cookie文件存在') || 
            line.includes('找到Token') || line.includes('Token有效期') || 
            line.includes('Token值有效') || line.includes('Cookie验证通过')) {
            inCookieSection = true;
            continue;
        }
        if (inCookieSection && (line.includes('===') || line.includes('请选择功能'))) {
            inCookieSection = false;
        }
        if (!inCookieSection) {
            filteredLines.push(line);
        }
    }
    
    text = filteredLines.join('\n');
    
    let formatted = text
        .replace(/^(.*✓.*)$/gm, '<span style="color: #67c23a;">$1</span>')
        .replace(/^(.*✗.*)$/gm, '<span style="color: #f56c6c;">$1</span>')
        .replace(/^(.*🔍.*)$/gm, '<span style="color: #409EFF;">$1</span>')
        .replace(/^(.*🔧.*)$/gm, '<span style="color: #E6A23C;">$1</span>')
        .replace(/^(.*⚠️.*)$/gm, '<span style="color: #E6A23C;">$1</span>')
        .replace(/^(.*✅.*)$/gm, '<span style="color: #67c23a;">$1</span>')
        .replace(/^(.*❌.*)$/gm, '<span style="color: #f56c6c;">$1</span>')
        .replace(/^(.*📊.*)$/gm, '<span style="color: #909399;">$1</span>')
        .replace(/^(.*¥[0-9,.]*.*)$/gm, '<span style="color: #E6A23C; font-weight: bold;">$1</span>')
        .replace(/^(.*预计.*)$/gm, '<span style="color: #E6A23C;">$1</span>')
        .replace(/^(.*耗时.*)$/gm, '<span style="color: #909399;">$1</span>')
        .replace(/^(.*保存.*)$/gm, '<span style="color: #409EFF;">$1</span>')
        .replace(/^(.*获取.*)$/gm, '<span style="color: #409EFF;">$1</span>')
        .replace(/^(.*成功.*)$/gm, '<span style="color: #67c23a;">$1</span>')
        .replace(/^(===.*===)$/gm, '<span style="color: #909399;">$1</span>')
        .replace(/^(---.*---)$/gm, '<span style="color: #909399;">$1</span>')
        .replace(/^(={50,})$/gm, '<span style="color: #909399;">$1</span>')
        .replace(/^(\s*\d+\/\s*\d+\s*页:.*)$/gm, '<span style="color: #409EFF;">$1</span>')
        .replace(/^(开始时间:|结束时间:|总运行时间:.*)$/gm, '<span style="color: #909399;">$1</span>')
        .replace(/^(开始运行...|浏览器启动耗时:|页面创建耗时:.*)$/gm, '<span style="color: #E6A23C;">$1</span>')
        .replace(/^(Cookie已保存|浏览器关闭耗时:.*)$/gm, '<span style="color: #67c23a;">$1</span>')
        .replace(/^(注意：|提示：.*)$/gm, '<span style="color: #909399; font-style: italic;">$1</span>')
        .replace(/^(请输入选项.*)$/gm, '<span style="color: #409EFF; font-weight: bold;">$1</span>')
        .replace(/^(\d+\.\s+.*)$/gm, '<span style="color: #333; font-weight: bold;">$1</span>')
        .replace(/^(对比文件:|新增商品数:|删除商品数:|新增高价商品数:.*)$/gm, '<span style="color: #E6A23C;">$1</span>')
        .replace(/^(输入货号总数:|JSON中货号总数:|已存在货号数:|缺失货号数:|JSON中多余货号数:|重复序列号数:.*)$/gm, '<span style="color: #E6A23C;">$1</span>');
    
    return formatted;
}

function showSkuInputPanel() {
    const skuPanel = document.getElementById('sku-input-panel');
    const skuContent = document.getElementById('sku-input-content');
    if (!skuPanel || !skuContent) return;
    skuPanel.style.display = 'block';
    skuPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    skuContent.innerHTML = `
        <div style="padding: 20px;">
            <div class="form-group">
                <label><strong>输入货号:</strong></label>
                <textarea id="sku-input" class="form-control" rows="10" placeholder="请输入货号，支持以下格式：&#10;• 每行一个货号&#10;• 用逗号分隔&#10;• 用空格分隔&#10;• 任意数字组合"></textarea>
            </div>
            <div class="form-group">
                <button id="btn-compare-sku" class="btn btn-primary btn-block" onclick="compareSku()">
                    <i class="fa fa-exchange"></i> 开始对比
                </button>
            </div>
            <div class="form-group">
                <small class="text-muted">
                    <i class="fa fa-info-circle"></i> 系统会自动提取输入中的所有数字作为货号进行对比
                </small>
            </div>
        </div>
    `;
}

function compareSku() {
    const skuInputEl = document.getElementById('sku-input');
    if (!skuInputEl) {
        alert('找不到输入框');
        return;
    }
    const skuInput = skuInputEl.value;
    if (!skuInput.trim()) {
        alert('请输入货号');
        return;
    }
    
    const btn = document.getElementById('btn-compare-sku');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> 对比中...';
    }
    
    fetch('/api/sku/compare/txt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ skus: skuInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('对比失败: ' + data.error);
            if (btn) {
                btn.disabled = false;
                btn.innerHTML = '<i class="fa fa-exchange"></i> 开始对比';
            }
            return;
        }
        
        showComparisonResult(data);
    })
    .catch(error => {
        alert('请求失败: ' + error.message);
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa fa-exchange"></i> 开始对比';
        }
    });
}

function showComparisonResult(data) {
    const skuPanel = document.getElementById('sku-input-panel');
    const skuContent = document.getElementById('sku-input-content');
    if (!skuPanel || !skuContent) return;
    
    skuPanel.style.display = 'block';
    skuPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    
    const existingCard = skuContent.querySelector('.comparison-card');
    if (existingCard) existingCard.remove();
    
    let cardHtml = `
    <div class="comparison-card">
        <div class="comparison-header" style="background: #E6A23C;">
            <i class="fa fa-barcode"></i> 货号对比结果
        </div>
        <div class="comparison-body">
            <div class="comparison-stats">
                <div class="stat-item ${data.txt_count > 0 ? 'stat-info' : ''}">
                    <span class="stat-value">${data.txt_count || 0}</span>
                    <span class="stat-label">输入货号</span>
                </div>
                <div class="stat-item ${data.extra_count > 0 ? 'stat-warning' : ''}">
                    <span class="stat-value">${data.extra_count || 0}</span>
                    <span class="stat-label">JSON多余</span>
                </div>
                <div class="stat-item ${data.json_count > 0 ? 'stat-info' : ''}">
                    <span class="stat-value">${data.json_count || 0}</span>
                    <span class="stat-label">JSON货号</span>
                </div>
                <div class="stat-item ${data.common_count > 0 ? 'stat-success' : ''}">
                    <span class="stat-value">${data.common_count || 0}</span>
                    <span class="stat-label">已存在</span>
                </div>
            </div>
            <div class="comparison-stats">
                <div class="stat-item ${data.missing_count > 0 ? 'stat-danger' : ''}">
                    <span class="stat-value">${data.missing_count || 0}</span>
                    <span class="stat-label">缺失货号</span>
                </div>
                <div class="stat-item ${data.duplicate_count > 0 ? 'stat-warning' : ''}">
                    <span class="stat-value">${data.duplicate_count || 0}</span>
                    <span class="stat-label">重复序列号</span>
                </div>
            </div>`;
    
    if (data.duplicates && data.duplicates.length > 0) {
        const dupItems = data.duplicates.map(d => `<span class="sku-tag" style="background: #ff9800; color: white;">${d.货号} (重复${d.count}次)</span>`).join('');
        cardHtml += `
            <div class="missing-skus" style="background: #fff3e0; border-color: #ff9800;">
                <div class="missing-title" style="color: #e65100;">重复货号列表:</div>
                <div class="sku-container">${dupItems}</div>
            </div>`;
    }
    
    if (data.missing_in_json && data.missing_in_json.length > 0) {
        const items = data.missing_in_json.map(sku => `<span class="sku-tag">${sku}</span>`).join('');
        cardHtml += `
            <div class="missing-skus" style="background: #ffebee; border-color: #ef9a9a;">
                <div class="missing-title" style="color: #c62828;">输入货号中JSON中不存在的货号:</div>
                <div class="sku-container">${items}</div>
            </div>`;
    }
    
    if (data.extra_in_json && data.extra_in_json.length > 0) {
        const items = data.extra_in_json.map(sku => `<span class="sku-tag" onclick="showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
        cardHtml += `
            <div class="missing-skus" style="background: #fff3e0; border-color: #ffb74d;">
                <div class="missing-title" style="color: #f57c00;">JSON中多余货号(有货但不在输入中):</div>
                <div class="sku-container">${items}</div>
            </div>`;
    }
    
    if (data.common && data.common.length > 0) {
        const items = data.common.map(sku => `<span class="sku-tag" onclick="console.log('[按钮点击] 查看商品详情:', '${sku}'); showProductDetail('${sku}')" style="cursor: pointer;">${sku}</span>`).join('');
        cardHtml += `
            <div class="missing-skus" style="background: #e8f5e9; border-color: #81c784;">
                <div class="missing-title" style="color: #388e3c;">共同货号:</div>
                <div class="sku-container">${items}</div>
            </div>`;
    }
    
    cardHtml += `</div></div>`;
    
    skuContent.insertAdjacentHTML('beforeend', cardHtml);
}

function showCleanerPanel() {
    const cleanerPanel = document.getElementById('cleaner-panel');
    const cleanerContent = document.getElementById('cleaner-content');
    if (!cleanerPanel || !cleanerContent) return;
    cleanerPanel.style.display = 'block';
    cleanerPanel.scrollIntoView({ behavior: 'smooth' });
    cleanerContent.innerHTML = `
        <div style="padding: 20px;">
            <div class="form-group">
                <label><strong>清理目录:</strong></label>
                <input type="text" id="clean-directory" class="form-control" value="" placeholder="请输入要清理的目录（留空使用当前目录）">
            </div>
            <div class="form-group">
                <label><strong>清理模式:</strong></label>
                <select id="clean-mode" class="form-control">
                    <option value="list">1. 列出文件（不删除）</option>
                    <option value="group">2. 按组清理（保留最新的一组文件）</option>
                    <option value="time">3. 按时间清理</option>
                    <option value="png">4. 删除PNG文件</option>
                    <option value="media">5. 删除媒体文件（PNG/JPG/GIF/MP4）</option>
                    <option value="all">6. 删除所有文件和文件夹</option>
                </select>
            </div>
            <div class="form-group" id="minutes-group" style="display: none;">
                <label><strong>时间阈值（分钟）:</strong></label>
                <input type="number" id="clean-minutes" class="form-control" value="5" min="1">
            </div>
            <div class="form-group">
                <label class="checkbox-inline">
                    <input type="checkbox" id="clean-dry-run" checked> 测试模式（不实际删除）
                </label>
            </div>
            <button id="btn-execute-clean" class="btn btn-danger btn-lg btn-block" style="margin-top: 20px;">
                <i class="fa fa-play"></i> 执行清理
            </button>
        </div>
        <div class="output-content" id="clean-output" style="display: none;"></div>
        <div class="output-status" id="clean-status"></div>
    `;
    
    const cleanModeEl = document.getElementById('clean-mode');
    const minutesGroupEl = document.getElementById('minutes-group');
    if (cleanModeEl) {
        cleanModeEl.addEventListener('change', function() {
            if (minutesGroupEl) minutesGroupEl.style.display = this.value === 'time' ? 'block' : 'none';
        });
    }
    
    const cleanBtn = document.getElementById('btn-execute-clean');
    if (cleanBtn) cleanBtn.addEventListener('click', executeClean);
}

function executeClean() {
    const modeEl = document.getElementById('clean-mode');
    const directoryEl = document.getElementById('clean-directory');
    const dryRunEl = document.getElementById('clean-dry-run');
    const minutesEl = document.getElementById('clean-minutes');
    const btn = document.getElementById('btn-execute-clean');
    const outputDiv = document.getElementById('clean-output');
    const statusDiv = document.getElementById('clean-status');
    
    const mode = modeEl ? modeEl.value : 'time';
    const directory = directoryEl ? directoryEl.value || '' : '';
    const dryRun = dryRunEl ? dryRunEl.checked : false;
    const minutes = minutesEl ? minutesEl.value || 5 : 5;
    
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> 执行中...';
    }
    
    if (outputDiv) {
        outputDiv.style.display = 'block';
        outputDiv.innerHTML = '<span style="color: #e6a23c;"><i class="fa fa-spinner fa-spin"></i> 正在执行...</span>';
    }
    
    let apiUrl = '';
    let data = { directory, dry_run: dryRun };
    
    switch(mode) {
        case 'list':
            apiUrl = '/api/clean/list';
            break;
        case 'group':
            apiUrl = '/api/clean/group';
            break;
        case 'time':
            apiUrl = '/api/clean/time';
            data.minutes = parseInt(minutes);
            break;
        case 'png':
            apiUrl = '/api/clean/png';
            break;
        case 'media':
            apiUrl = '/api/clean/media';
            break;
        case 'all':
            apiUrl = '/api/clean/all';
            break;
    }
    
    fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            if (outputDiv) outputDiv.innerHTML = '<pre style="margin: 0; white-space: pre-wrap; word-break: break-all;">' + formatOutput(result.output) + '</pre>';
            if (statusDiv) statusDiv.innerHTML = '<span style="color: #67c23a;">✓ 执行完成</span>';
        } else {
            if (outputDiv) outputDiv.innerHTML = '<span style="color: #f56c6c;">✗ 执行失败: ' + result.error + '</span>';
            if (statusDiv) statusDiv.innerHTML = '<span style="color: #f56c6c;">✗ 执行失败</span>';
        }
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa fa-play"></i> 执行清理';
        }
    })
    .catch(error => {
        if (outputDiv) outputDiv.innerHTML = '<span style="color: #f56c6c;">✗ 请求失败: ' + error.message + '</span>';
        if (statusDiv) statusDiv.innerHTML = '<span style="color: #f56c6c;">✗ 请求失败</span>';
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fa fa-play"></i> 执行清理';
        }
    });
}

// ==================== Hostc Tunnel ====================
function initHostcTunnel() {
    loadServerInfo();
    checkTunnelStatus();
    setInterval(checkTunnelStatus, 2000);
}

async function loadServerInfo() {
    try {
        const response = await fetch('/api/server/info');
        const data = await response.json();
        if (data.success) {
            const localUrlEl = document.getElementById('tunnel-local-url');
            const lanUrlEl = document.getElementById('tunnel-lan-url');
            if (localUrlEl) localUrlEl.textContent = data.local_url;
            if (data.lan_url && lanUrlEl) {
                lanUrlEl.textContent = data.lan_url;
                if (lanUrlEl.parentElement) lanUrlEl.parentElement.style.display = 'block';
            }
            // 更新页面版本号
            if (data.version) {
                document.querySelectorAll('.badge-version, .page-version').forEach(el => {
                    el.textContent = '版本: ' + data.version;
                });
                document.querySelectorAll('p.text-muted').forEach(el => {
                    if (el.textContent.includes('版本:')) {
                        el.textContent = '版本: ' + data.version;
                    }
                });
            }
        }
    } catch (e) {
        console.error('获取服务器信息失败:', e);
    }
}

async function checkTunnelStatus() {
    try {
        const response = await fetch('/api/tunnel/status');
        const data = await response.json();
        updateTunnelUI(data.running, data.url, data.auto_restart, data.restart_count, data.last_error, data.tunnel_type);
    } catch (e) {
        console.error('检查隧道状态失败:', e);
    }
}

function updateTunnelUI(running, url, autoRestart, restartCount, lastError, tunnelType) {
    const btn = document.getElementById('btn-toggle-tunnel');
    const status = document.getElementById('tunnel-status');
    const urlDisplay = document.getElementById('tunnel-public-url');
    const restartInfo = document.getElementById('tunnel-restart-info');
    const tunnelTypeDisplay = document.getElementById('tunnel-type');
    
    // 显示隧道类型
    if (tunnelTypeDisplay) {
        tunnelTypeDisplay.innerHTML = '<span class="text-success"><i class="fa fa-bolt"></i> hostc</span>';
    }
    
    if (btn) {
        if (running && url) {
            btn.className = 'btn btn-secondary';
            btn.innerHTML = '<i class="fa fa-check"></i> 隧道运行中';
            btn.disabled = true;
        } else {
            btn.className = 'btn btn-success';
            btn.innerHTML = '<i class="fa fa-play"></i> 启动隧道';
            btn.disabled = false;
        }
    }
    
    if (status) {
        if (running && url) {
            status.innerHTML = '<span class="badge badge-success"><i class="fa fa-circle"></i> 已连接</span>';
        } else {
            if (restartCount > 0) {
                status.innerHTML = '<span class="badge badge-warning"><i class="fa fa-refresh fa-spin"></i> 正在重连...</span>';
            } else {
                status.innerHTML = '<span class="badge badge-secondary"><i class="fa fa-circle"></i> 未连接</span>';
            }
        }
    }
    
    if (urlDisplay) {
        if (url) {
            urlDisplay.innerHTML = `<a href="${url}" target="_blank" class="text-primary font-weight-bold">${url}</a>`;
            if (urlDisplay.parentElement) {
                urlDisplay.parentElement.style.display = 'block';
            }
        } else {
            if (urlDisplay.parentElement) {
                urlDisplay.parentElement.style.display = 'none';
            }
        }
    }
    
    if (restartInfo) {
        if (restartCount > 0 || lastError) {
            let infoHtml = '';
            if (restartCount > 0) {
                infoHtml += `<span class="text-info"><i class="fa fa-refresh"></i> 已自动重连 ${restartCount} 次</span>`;
            }
            if (lastError) {
                infoHtml += `<br><small class="text-muted">最近错误: ${lastError}</small>`;
            }
            restartInfo.innerHTML = infoHtml;
            restartInfo.style.display = 'block';
        } else {
            restartInfo.style.display = 'none';
        }
    }
}

async function toggleTunnel() {
    const btn = document.getElementById('btn-toggle-tunnel');
    const status = document.getElementById('tunnel-status');
    if (btn) btn.disabled = true;
    if (status) status.innerHTML = '<span class="badge badge-warning"><i class="fa fa-spinner fa-spin"></i> 处理中...</span>';
    
    try {
        const response = await fetch('/api/tunnel/status');
        const data = await response.json();

        if (!data.running) {
            const startRes = await fetch('/api/tunnel/start', { method: 'POST' });
            const startData = await startRes.json();
            if (startData.success) {
                // 如果返回了 URL，直接显示
                if (startData.url) {
                    checkTunnelStatus();
                } else {
                    // 持续轮询直到获取到 URL
                    const pollInterval = setInterval(async () => {
                        const statusRes = await fetch('/api/tunnel/status');
                        const statusData = await statusRes.json();
                        if (statusData.url) {
                            clearInterval(pollInterval);
                            checkTunnelStatus();
                        }
                    }, 1000);
                    // 最多轮询 30 秒
                    setTimeout(() => clearInterval(pollInterval), 30000);
                    checkTunnelStatus();
                }
            } else {
                alert('启动失败: ' + (startData.error || '未知错误'));
                checkTunnelStatus();
            }
        }
    } catch (e) {
        alert('操作失败: ' + e.message);
        checkTunnelStatus();
    }
}

function showTunnelSection() {
    console.log('[隧道管理] 显示隧道管理面板');
    const tunnelPanel = document.getElementById('tunnel-panel');
    const tunnelContent = document.getElementById('tunnel-content');
    if (!tunnelPanel || !tunnelContent) return;
    
    tunnelPanel.style.display = 'block';
    tunnelPanel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    
    console.log('[隧道管理] 渲染隧道管理界面');
    tunnelContent.innerHTML = `
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h4 class="mb-0"><i class="fa fa-external-link"></i> 隧道共享</h4>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <div class="info-section mb-4">
                            <h5><i class="fa fa-server"></i> 本地服务</h5>
                            <div class="alert alert-info mb-2">
                                <i class="fa fa-desktop"></i> <strong>本地地址:</strong> 
                                <span id="tunnel-local-url" class="font-weight-bold">加载中...</span>
                            </div>
                            <div class="alert alert-info" style="display: none;">
                                <i class="fa fa-globe"></i> <strong>局域网地址:</strong> 
                                <span id="tunnel-lan-url" class="font-weight-bold"></span>
                                <small class="text-muted ml-2">(同一网络下的设备可访问)</small>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="info-section mb-4">
                            <h5><i class="fa fa-cloud"></i> 公网隧道</h5>
                            <div class="alert alert-light border mb-2">
                                <i class="fa fa-info-circle"></i> <strong>隧道类型:</strong> 
                                <span id="tunnel-type" class="font-weight-bold">加载中...</span>
                            </div>
                            <div id="tunnel-status-display" class="mb-2">
                                <span id="tunnel-status"><span class="badge badge-secondary"><i class="fa fa-circle"></i> 未连接</span></span>
                                <div id="tunnel-restart-info" class="mt-1" style="display: none;"></div>
                            </div>
                            <div class="alert alert-success" id="tunnel-url-section" style="display: none;">
                                <i class="fa fa-link"></i> <strong>公网地址:</strong><br>
                                <span id="tunnel-public-url"></span>
                                <small class="text-muted d-block mt-1">复制链接分享给其他人，他们可以通过这个地址访问你的本地服务</small>
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
                <div class="text-center">
                    <button id="btn-toggle-tunnel" class="btn btn-success btn-lg" onclick="console.log('[按钮点击] 切换隧道状态'); toggleTunnel()">
                        <i class="fa fa-play"></i> 启动隧道
                    </button>
                </div>
                <div class="mt-4">
                    <div class="alert alert-warning">
                        <i class="fa fa-info-circle"></i> <strong>使用说明:</strong>
                        <ul class="mb-0 mt-2">
                            <li>点击"启动隧道"按钮，将本地服务暴露到公网</li>
                            <li>生成公网地址后，可以复制链接分享给其他人</li>
                            <li>公网地址仅在隧道运行时有效，关闭后会失效</li>
                            <li>默认使用 <code>hostc</code> 隧道服务</code></li>
                            <li>确保网络连接正常</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    `;
    loadServerInfo();
    checkTunnelStatus();
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', initHostcTunnel);