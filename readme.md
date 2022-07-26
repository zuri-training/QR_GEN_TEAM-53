# QR CODE GENERATOR - Team 53 solution


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
- [Author](#author)



## Overview

### The challenge

Users should be able to:

- View the optimal layout depending on their device's screen size
- See hover and focus states for interactive elements


### Links

- Solution URL: [Add solution URL here](https://your-solution-url.com)
- Live Site URL: [Add live site URL here](https://your-live-site-url.com)

## My process

### Built with

- Semantic HTML5 markup
- CSS custom properties
- CSS Grid
- Mobile-first workflow


### What I learned

```html
<p class="price"> <p id="new-price">$149.99</p>
        <strike><p id="old-price">$169.99</p></strike>
      </p>
```
```css
.btn:hover {
    font-family: 'Montserrat', sans-serif; 
    background: var(--darker);
    text-decoration: none;
}
```
```JS
<script>
    if(screen.width <= 380){
      document.getElementById("goods").src="images/image-product-mobile.jpg"
    }
  </script>
```


### Author

- Frontend Mentor - [@yourusername](https://www.frontendmentor.io/profile/yourusername)
- Twitter - [@yourusername](https://www.twitter.com/yourusername)
