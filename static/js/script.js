document.addEventListener("DOMContentLoaded", function(){


    console.log(
        "Cloud Sandbox Portal Loaded"
    );


    // Button animation

    const buttons = document.querySelectorAll(".btn-primary");


    buttons.forEach(button => {


        button.addEventListener(
            "mouseenter",
            function(){

                button.style.transform =
                "scale(1.05)";

            }
        );


        button.addEventListener(
            "mouseleave",
            function(){

                button.style.transform =
                "scale(1)";

            }
        );


    });





    // Auto update deployment status appearance

    const statusBadges =
    document.querySelectorAll(".badge");


    statusBadges.forEach(
        badge => {


        if(
            badge.innerText
            .toLowerCase()
            .includes("provisioning")
        )
        {

            badge.style.animation =
            "pulse 2s infinite";

        }


    });



});
