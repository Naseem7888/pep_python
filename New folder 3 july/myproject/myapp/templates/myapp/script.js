document.addEventListener('DOMContentLoaded', () => {

    // --- 3D HERO BACKGROUND (for home page) ---
    const heroCanvas = document.getElementById('hero-3d-background');
    if (heroCanvas) {
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ canvas: heroCanvas, alpha: true });

        renderer.setSize(window.innerWidth, window.innerHeight);
        camera.position.z = 5;

        // Particles
        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 5000;
        const posArray = new Float32Array(particlesCount * 3);

        for (let i = 0; i < particlesCount * 3; i++) {
            posArray[i] = (Math.random() - 0.5) * 10;
        }

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        const particlesMaterial = new THREE.PointsMaterial({
            size: 0.008,
            color: 0x00f0f0,
        });
        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);

        // Animation loop
        const animate = () => {
            requestAnimationFrame(animate);
            particlesMesh.rotation.y += 0.0005;
            particlesMesh.rotation.x += 0.0002;
            renderer.render(scene, camera);
        };
        animate();

        // Handle window resize
        window.addEventListener('resize', () => {
            renderer.setSize(window.innerWidth, window.innerHeight);
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
        });
    }

    // --- GSAP ANIMATIONS ---
    gsap.registerPlugin(ScrollTrigger);

    // General timeline for fade-in animations
    const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    // Hero Section Animation (if it exists)
    if (document.querySelector('.hero-content')) {
        tl.to('.hero h1', { opacity: 1, y: 0, duration: 1, delay: 0.5 })
          .to('.hero p', { opacity: 1, y: 0, duration: 1 }, '-=0.7')
          .to('.cta-button', { opacity: 1, y: 0, duration: 1 }, '-=0.7');
    }

    // Features Section Scroll-Triggered Animation
    const animatedSection = document.querySelector('.animated-section');
    if (animatedSection) {
        gsap.fromTo(animatedSection.querySelector('h2'),
            { opacity: 0, y: 30 },
            {
                opacity: 1,
                y: 0,
                duration: 1,
                scrollTrigger: {
                    trigger: animatedSection,
                    start: 'top 80%',
                    toggleActions: 'play none none none'
                }
            }
        );

        gsap.fromTo('.feature-item',
            { opacity: 0, y: 30 },
            {
                opacity: 1,
                y: 0,
                duration: 0.8,
                stagger: 0.2,
                scrollTrigger: {
                    trigger: '.feature-grid',
                    start: 'top 80%',
                    toggleActions: 'play none none none'
                }
            }
        );
    }

    // Contact Page Animations (if it exists)
    const contactSection = document.querySelector('.contact-section');
    if (contactSection) {
        const contactTl = gsap.timeline({
            defaults: { ease: 'power3.out' },
            scrollTrigger: {
                trigger: contactSection,
                start: 'top 70%',
                toggleActions: 'play none none none'
            }
        });

        contactTl.to('.contact-section h1', { opacity: 1, y: 0, duration: 1 })
                 .to('.contact-section p', { opacity: 1, y: 0, duration: 1 }, '-=0.8')
                 .to('.contact-card', { opacity: 1, scale: 1, duration: 1.2 }, '-=0.8');
    }
});