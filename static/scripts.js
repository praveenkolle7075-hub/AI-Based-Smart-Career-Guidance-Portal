/* =====================================================
   CAREER AI - MAIN JAVASCRIPT
===================================================== */


/* =====================================================
   FORM VALIDATION
===================================================== */

function validateForm() {

    const fields = [
        "math",
        "programming",
        "communication",
        "creativity",
        "analytical",
        "leadership"
    ];

    for (let field of fields) {

        const element =
            document.getElementById(field);

        if (!element) {
            continue;
        }

        const value =
            Number(element.value);

        if (
            isNaN(value) ||
            value < 0 ||
            value > 100
        ) {

            alert(
                "Please enter a value between 0 and 100."
            );

            element.focus();

            return false;
        }
    }

    return true;
}


/* =====================================================
   SCROLL REVEAL
===================================================== */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const elements =
            document.querySelectorAll(".reveal");

        elements.forEach(
            function (element, index) {

                element.style.animationDelay =
                    (index * 0.08) + "s";

            }
        );

    }
);


/* =====================================================
   BUTTON LOADING
===================================================== */

document.addEventListener(
    "submit",
    function (event) {

        const button =
            event.target.querySelector(
                'button[type="submit"]'
            );

        if (!button) {
            return;
        }

        setTimeout(
            function () {

                button.innerHTML =
                    '<i class="bi bi-cpu me-2"></i> AI Analyzing...';

                button.disabled = true;

            },
            50
        );

    }
);


/* =====================================================
   MOUSE GLOW
===================================================== */

document.addEventListener(
    "mousemove",
    function (event) {

        const x =
            event.clientX;

        const y =
            event.clientY;

        document.documentElement.style
            .setProperty(
                "--mouse-x",
                x + "px"
            );

        document.documentElement.style
            .setProperty(
                "--mouse-y",
                y + "px"
            );

    }
);


/* =====================================================
   INPUT HOVER EFFECT
===================================================== */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        const inputs =
            document.querySelectorAll(
                ".form-control"
            );

        inputs.forEach(
            function (input) {

                input.addEventListener(
                    "focus",
                    function () {

                        this.parentElement
                            .classList.add(
                                "input-active"
                            );

                    }
                );

                input.addEventListener(
                    "blur",
                    function () {

                        this.parentElement
                            .classList.remove(
                                "input-active"
                            );

                    }
                );

            }
        );

    }
);


/* =====================================================
   SMOOTH ANCHOR LINKS
===================================================== */

document.querySelectorAll(
    'a[href^="#"]'
).forEach(
    function (anchor) {

        anchor.addEventListener(
            "click",
            function (event) {

                const target =
                    document.querySelector(
                        this.getAttribute("href")
                    );

                if (target) {

                    event.preventDefault();

                    target.scrollIntoView({
                        behavior: "smooth"
                    });

                }

            }
        );

    }
);