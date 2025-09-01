// Initialize Telegram WebApp
let tg = window.Telegram.WebApp;

// Initialize the app
tg.ready();
tg.expand();

// Set the main button color to match our theme
tg.MainButton.setParams({
    text: 'Join Giveaway',
    color: '#667eea',
    text_color: '#ffffff'
});

// DOM elements
const walletInput = document.getElementById('wallet');
const claimBtn = document.getElementById('claimBtn');
const resultModal = document.getElementById('resultModal');
const modalTitle = document.getElementById('modalTitle');
const modalMessage = document.getElementById('modalMessage');
const closeModal = document.getElementById('closeModal');

// Wallet address validation
function isValidWalletAddress(address) {
    // Basic Ethereum address validation
    const ethAddressRegex = /^0x[a-fA-F0-9]{40}$/;
    return ethAddressRegex.test(address);
}

// Show modal with custom content
function showModal(title, message) {
    modalTitle.textContent = title;
    modalMessage.textContent = message;
    resultModal.style.display = 'block';
    
    // Add haptic feedback if available
    if (tg.HapticFeedback) {
        tg.HapticFeedback.impactOccurred('medium');
    }
}

// Hide modal
function hideModal() {
    resultModal.style.display = 'none';
}

// Handle claim button click
claimBtn.addEventListener('click', function() {
    const walletAddress = walletInput.value.trim();
    
    // Validate wallet address
    if (!walletAddress) {
        showModal('⚠️ Error', 'Please enter your wallet address!');
        return;
    }
    
    if (!isValidWalletAddress(walletAddress)) {
        showModal('⚠️ Invalid Address', 'Please enter a valid Ethereum wallet address (0x...)!');
        return;
    }
    
    // Add loading state
    claimBtn.classList.add('loading');
    claimBtn.disabled = true;
    
    // Simulate processing delay
    setTimeout(() => {
        // Remove loading state
        claimBtn.classList.remove('loading');
        claimBtn.disabled = false;
        
        // Show the prank message
        showModal('🎉 Chúc mừng!', 'Bạn bị lừa rồi haha! 😂\n\nĐây chỉ là một trò đùa thôi. Cảm ơn bạn đã tham gia!');
        
        // Send data to Telegram (optional)
        if (tg.sendData) {
            tg.sendData(JSON.stringify({
                action: 'claim_attempted',
                wallet: walletAddress,
                timestamp: new Date().toISOString()
            }));
        }
        
        // Show notification in Telegram
        tg.showAlert('Bạn bị lừa rồi! 😄');
        
    }, 2000);
});

// Close modal when clicking the close button
closeModal.addEventListener('click', hideModal);

// Close modal when clicking outside
resultModal.addEventListener('click', function(e) {
    if (e.target === resultModal) {
        hideModal();
    }
});

// Handle wallet input validation
walletInput.addEventListener('input', function() {
    const address = this.value.trim();
    if (address && isValidWalletAddress(address)) {
        this.style.borderColor = '#4CAF50';
    } else if (address) {
        this.style.borderColor = '#ff6b6b';
    } else {
        this.style.borderColor = '#e1e5e9';
    }
});

// Handle Telegram button click
document.querySelector('.telegram-btn').addEventListener('click', function() {
    // Open Telegram link
    tg.openTelegramLink('https://t.me/asteroid_community');
    
    // Show notification
    tg.showAlert('Opening Telegram Community...');
});

// Add some fun animations
document.addEventListener('DOMContentLoaded', function() {
    // Animate elements on load
    const elements = document.querySelectorAll('.giveaway-card, .header');
    elements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            el.style.transition = 'all 0.6s ease';
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 200);
    });
    
    // Add confetti effect on page load (optional)
    setTimeout(() => {
        createConfetti();
    }, 1000);
});

// Simple confetti effect
function createConfetti() {
    const colors = ['#ff6b6b', '#4CAF50', '#667eea', '#ffd700', '#ff69b4'];
    
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            const confetti = document.createElement('div');
            confetti.style.position = 'fixed';
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.top = '-10px';
            confetti.style.width = '10px';
            confetti.style.height = '10px';
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.borderRadius = '50%';
            confetti.style.pointerEvents = 'none';
            confetti.style.zIndex = '9999';
            confetti.style.animation = 'fall 3s linear forwards';
            
            document.body.appendChild(confetti);
            
            // Remove confetti after animation
            setTimeout(() => {
                confetti.remove();
            }, 3000);
        }, i * 100);
    }
}

// Add fall animation CSS
const style = document.createElement('style');
style.textContent = `
    @keyframes fall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Handle back button
tg.BackButton.onClick(() => {
    if (resultModal.style.display === 'block') {
        hideModal();
    } else {
        tg.close();
    }
});

// Show back button when modal is open
function showBackButton() {
    tg.BackButton.show();
}

function hideBackButton() {
    tg.BackButton.hide();
}

// Update back button visibility when modal opens/closes
const originalShowModal = showModal;
showModal = function(title, message) {
    originalShowModal(title, message);
    showBackButton();
};

const originalHideModal = hideModal;
hideModal = function() {
    originalHideModal();
    hideBackButton();
};

// Initialize back button state
hideBackButton();
