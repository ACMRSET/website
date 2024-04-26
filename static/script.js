
const navbar = document.querySelector("#navbar");
const acmlogo = document.querySelector("#acm-img");
const rsetlogo = document.querySelector(".nav-div .rset-div img");
const heading = document.querySelector(".heading-div")

window.addEventListener('scroll', () => {
    console.log(window.scrollY);
    // window.scrollY > 10 
    //     ? navbar.classList.add('small') 
    //     : navbar.classList.remove('small')


    if (window.scrollY > 20) {
        navbar.classList.add('small') 
        acmlogo.classList.add('shrink-acm')
        rsetlogo.classList.add('d-none')
        heading.classList.add('hide-heading')
    }
    else{
        navbar.classList.remove('small')
        acmlogo.classList.remove('shrink-acm')
        rsetlogo.classList.remove('d-none')
        heading.classList.remove('hide-heading')
    }
})