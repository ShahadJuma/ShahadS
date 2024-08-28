// Example JavaScript to update card information
function updateInfo() {
    // In a real-world scenario, you might fetch this data from an API or a form
    const newInfo = {
        name: 'Jane Smith',
        title: 'Web Developer',
        email: 'jane.smith@example.com',
        phone: '+098 765 4321',
        profilePic: 'jane-smith.png' // Replace with the path to a new profile picture
    };

    document.getElementById('name').textContent = newInfo.name;
    document.getElementById('title').textContent = newInfo.title;
    document.getElementById('email').textContent = newInfo.email;
    document.getElementById('phone').textContent = newInfo.phone;
    document.getElementById('profile-pic').src = newInfo.profilePic;
}

// Ensure the script runs after the DOM has loaded
document.addEventListener('DOMContentLoaded', (event) => {
    // You can initialize or set up event listeners here if needed
    console.log('Document is ready');
});