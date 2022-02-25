# skate-shop
---------
![Responsive  Image](assets/img/)

---------
## User Experience (UX)

## User Stories

I want to view a list of products and view individual product details so i can find products and then look at specific deatils about them.

I want to view all purchases in a basket/shopping cart so i can easily see what im buying and find out how much i will spend.

I want to be able to create an account, login/logout, recover password and personalise my profile, this will allow me to log purchase history and save payment details.

I want to  sort by a list of available products, a specific category of product, multiple categories simultaniously, search for a product by name, easily see whats been searched and how many results, and select the size and quanity of the product. I want to be able to do all of this because it will make it easier for me to find specific items that i want to look for, each option will allow me to find the best products and products that fit my specific requirements.

I want to be able to adjust the ammount of items In my bag so i can easily make changes before i puchase the items in my basket.

I want to easily enter my payment info so I can check out easily without hassle.

I want to feel my info is secure so i can have confidence in the website and provide payment info with out leaks or breeches.

I want to view an order confirmation and an email confirmation after checkout which will verify that I've bought the goods i wanted to buy.

## Owner stories

I want to add a product to the website so i can add new items to my store.

I want to be able to edit/update a product so i can change product prices and details easily.

I want to have a safe and secure payment system so that i can take payments without a worry of breaches, which will allow me to operatea successfull business.

I want to be able to delete a product so i can remove items that are no longer for sale.

## Strategy Plane
The purpose of the website is to create an ecommerce website for a skating brand to sell skating products and clothes.

## Colour Scheme

## Typeography

---------
## Wire Frames
![Wire Frame](assets/img/)

---------
## Features

* Login/Logout/Register/Profiles
* Shopping cart
* Checkout/Payment system(Stripe)
* Products database
* Product pages + individual product details pages
* Search functionality within the store
* Responsive on all devices
* Easy to use navigation
* About section
* Contact page
* Product management
* Blog page

--------
## Structure

The website should be easy to use and simple to understand, it should be intuitive and enjoyable to use, which the structure should represent.

* Home page

    The home page is simple and welcoming presenting itself to the user in a stylish and appropriate manor, i went with simplistic design that focuses on readability and ease of use, for example, adequate spacing and not littering the home page with things to look at which would overload the users mind.

    #### Contents of the home page

    * Simple artistic welcome photo
    * A call to action in the form of reccomending the user visit the store 
    * Button that send the user to the store under neath the call to action
    * Navbar
    * Banner displaying a special dea lto increase customers desires to buy items

* Store

    The store is easy to navigate, with plenty of search and sort options. This was done by having sort by rating, price and category, the search function sorts by category and product name.

    #### Contents of the store page

    * Nav bar
    * Banner displaying a special dea lto increase customers desires to buy items
    * Products
    * Sort options
    * Update and delete functionality that only the admin can see

* Product details

    The product details page focuses on the details of the individual product and sell the item to the user. This was done by having a description, a product photo, a rating, category type, a price and add to cart, This is everything a customer should need to make a descision on wether to purchase an item or not.

    #### Contents of the product details page

    * Nav bar
    * Banner displaying a special dea lto increase customers desires to buy items
    * Product details(description)
    * Product photo
    * Product rating
    * Category type
    * Product price
    * Add to cart

* Toasts

    The toasts inform the user of any action that the customer makes, such as added an item to the cart, or login and log out of the users account. This was done for adding and removing a product from the cart, purchasing an item, registering an account, loggin in and  out, this also includes warnings and errors with anyhting that may go wrong with the site.

* Profiles

    The profile is made up of 2 parts, a form for the users address and a product history. The address form is to speed up checkout times as when the form is filled out and saved, it will automatically fill in the checkout form in for you, all you need to do is fill in the payment details. The order history is to help the user see what they bought from us before, for example, if they cant remember the parts they bought and need the same parts again, they can visit this section and see waht they ahve bought before.

    #### Contents of the profiles page

    * Navbar
    * User address
    * Order history

* Shopping cart and checkout

    The shopping cart is easy to understand, it tells the user what they will buy and how much it will cost, featuring a breakdown of the payment, such as delivery cost and total price for the items.

    #### Contents of the Shopping cart page

    * Navbar
    * What the user will buy
    * Continue to payment button 
    * Go back to products button


* Checkout

    The checkout is the same as the shopping cart except with a form for the users address and payment details and also inform the user of what they are buying with a price breakdown in the same way as the shopping cart page.

    #### Contents of the Shopping cart page

    * Navbar
    * Delivery form
    * What the user will buy

* Product management

    The product management is a simple to use page for the admin to add, create and delete products without accessing the backend of the website, it features add create and delete options which are clearly marked and has a form featuring everything that the admin will need to set up a product to be sold to the customers.

    #### Contents of the Product management page
    * Navbar
    * Product form
    * Save and delete options

* About us

    The about us section has a summary of who we are and why we do what we do, it also features an ethos designed to appeal to the cutomer and set the customer base.

    #### Contents of the about us page

    * Paragraphs detailing who we are and what we do and why
    * Social media links to give the user more content to view and to conenct with us on different platforms

* Contact us

    The contact us page is for people who have questions about a product or need to check something about the store, its a simple form that when filled out will be sent to the email of the person who can answer the questions the customer asks.

    #### Contents of the about us page
    * Contact form, Email, subject and message with a submit box

* Blog page

    The blog page is to Provide the customers and the users more content for them to consume, which will bring in more traffic and there for increase sales. The blog is a very useful marketing strategy as it help build personal relationships with users and customers which means that they will be more likely to buy products from the store if trust and a relationship is built with them.

    #### Contents of the Blog page
    * Nav bar
    * Blog Posts

---------

## Technologies Used
* HTML
    * HTML is used to create the skeleton of the website and to lay down the fundementals that build the website.
* CSS
    * CSS is used to style the website and to provide individual style to specific elements.
* JavaScript
    * JavaScript is used to bring interactive functionality into the website,
* Jquery
    * Jquery is a simpler version of JavaScript which for this project is used to simplify and shorten the JavaScript code.
* Balsamiq
    * Balsamiq has been used to design the wireframe
* GNU Image Manipulation
    * This is a Free to use image manipulation software that has been used to crop and edit the background image and images in the README file.
* Git
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* GitHub
    * GitHub is used to store the projects code after being pushed from Git.
* Python
    * Used for backend elements and to write the logic that makes the website function
* Django
    * Django is a webdevelopment framework and is a templating language that is used when there is a high volume of information being fed through the html pages
* Heroku
    * Used to deploy and host the website
* Bootstrap
    * Bootstrap was used to customise the webpage and allows me to easily implement consistent designs
* Fontawesome
    * Fontawesome was used to implement icons throughout the website
* SQLite
    * The data base used to house the products on the website
* Stripe
    * The payment platform of choice that was used in this site


---------

## Testing

### HTML validation

![HTML Validation](assets/img/)

### CSS Validation

![CSS Validation ](assets/img/)

### JavaScript Validation

![JavaScript Validation](assets/img/)

## For more testing click the link below

 [CLICK ME FOR MORE TESTING ](testing.md) 

---------
## Deployment

### Deploying to GitHub Pages

1. Log in to GitHub and find the GitHub repository
2. At the top of the repository, click on the "Settings" button in the menu.
3. In the Settings page scroll down until you find the "Pages" area.
4. Click on the link in the "Pages" section, which will send you to the dedicated tab.
5. then, in the "Source" area, click the dropdown called "None" then select "Master Branch".
6. The page will automatically refresh.
7. Finally, scroll down the page to locate the newly published site in the "GitHub Pages" section.

## Forking the Repositiory

Forking the GitHub repository makes a copy of the original repository on your GitHUb account, which allows you to make changes to the document wihtout changing the original repository. If you wish to make a clone, follow these steps on how ot do it:

1. Log in to your GitHub account and find the repository.
2. At the top of the repository above the "Settings" button on the menu, find and click the "Fork" button.
3. After clicking the "Fork" button, You will now have a copy of the original repository in your GitHub account.

## Making a Local Clone of the Repository

1. Log in to GitHub and find the GitHub repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and paste the URL that you copied in Step 3.
    * Your code should look like this: `$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
7. Press Enter and then your local clone will be created.
---------
## What To Improve Or Add

---------
## Issues when making the project

During the creation of the project I discovered that my secret key was exposed and needed to remove the secret key which was in my main settings.py file and make a new secret key and relocate it to my env.py file which is a secure file not accessible out side of the workspace.

---------
## Credits
