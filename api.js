// api.js - загрузка данных для главной страницы

const API_URL = 'http://localhost:5000/api';

// Загрузка портфолио
async function loadPortfolio() {
    try {
        const response = await fetch(`${API_URL}/portfolio`);
        const photos = await response.json();
        const container = document.getElementById('portfolioCarousel');
        if (container) {
            container.innerHTML = '';
            photos.forEach(photo => {
                container.innerHTML += `
                    <div class="portfolio-carousel-item">
                        <img src="${photo.image_url}" alt="${photo.title || 'Работа'}">
                    </div>
                `;
            });
        }
    } catch (error) {
        console.error('Ошибка загрузки портфолио:', error);
    }
}

// Загрузка видео
async function loadClips() {
    try {
        const response = await fetch(`${API_URL}/videos`);
        const videos = await response.json();
        const container = document.getElementById('clipsCarousel');
        if (container) {
            container.innerHTML = '';
            videos.forEach(video => {
                container.innerHTML += `
                    <div class="clip-item">
                        <video src="${video.video_url}" autoplay loop muted playsinline></video>
                    </div>
                `;
            });
        }
    } catch (error) {
        console.error('Ошибка загрузки видео:', error);
    }
}

// Отзывы - статические картинки
function loadReviews() {
    const reviewsContainer = document.getElementById('reviewsContainer');
    if (reviewsContainer) {
        reviewsContainer.innerHTML = `
            <div class="reviews-col col-left">
                <div class="review-box item-2 short-box">
                    <img src="review2.png" alt="Отзыв 2" class="review-img">
                </div>
            </div>
            <div class="reviews-col col-center">
                <div class="review-box item-3 medium-box">
                    <img src="review3.png" alt="Отзыв 3" class="review-img">
                </div>
            </div>
            <div class="reviews-col col-right">
                <div class="review-box item-5 medium-box">
                    <img src="review5.png" alt="Отзыв 5" class="review-img">
                </div>
            </div>
        `;
    }
}

// Загрузка цен на услуги
async function loadServicePrices() {
    try {
        const response = await fetch(`${API_URL}/services`);
        const services = await response.json();
        const hairService = services.find(s => s.name === 'Прическа');
        const makeupService = services.find(s => s.name === 'Макияж');

        if (hairService) {
            const hairElement = document.getElementById('hairPrice');
            if (hairElement) hairElement.textContent = `${hairService.price} РУБ`;
        }
        if (makeupService) {
            const makeupElement = document.getElementById('makeupPrice');
            if (makeupElement) makeupElement.textContent = `${makeupService.price} РУБ`;
        }
    } catch (error) {
        console.error('Ошибка загрузки цен:', error);
    }
}

// Загрузка цен на выезд
async function loadVisitPrices() {
    try {
        const response = await fetch(`${API_URL}/visit-prices`);
        const prices = await response.json();

        const severodvinsk = prices.find(p => p.city === 'Северодвинск');
        const arkhangelsk = prices.find(p => p.city === 'Архангельск');
        const early = prices.find(p => p.is_early === true);

        if (severodvinsk) {
            const element = document.getElementById('severodvinskPrice');
            if (element) element.textContent = `${severodvinsk.price} РУБ`;
        }
        if (arkhangelsk) {
            const element = document.getElementById('arkhangelskPrice');
            if (element) element.textContent = `${arkhangelsk.price} РУБ`;
        }
        if (early) {
            const element = document.getElementById('earlyPrice');
            if (element) element.textContent = `${early.price} РУБ`;
        }
    } catch (error) {
        console.error('Ошибка загрузки цен на выезд:', error);
    }
}

// Запуск всех загрузок при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    loadPortfolio();
    loadClips();
    loadReviews();
    loadServicePrices();
    loadVisitPrices();
});