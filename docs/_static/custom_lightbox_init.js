// _static/custom_lightbox_init.js

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Fancybox on all elements that have the data-fancybox attribute
    // And ensure it can handle videos
    if (typeof Fancybox !== 'undefined') {
        Fancybox.bind("[data-fancybox]", {
            // Optional: add configuration options here
            // For example, to enable fullscreen on open (often good for videos)
            // fullscreen: {
            //     autoStart: true,
            // },
            // You can also specify the type explicitly if needed, but Fancybox is usually smart
            // type: "video",
        });
    }
});