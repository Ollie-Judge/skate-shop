# Testing

To test the responsiveness of my site, i used Chrome devtools. This makes sure that the site is run on a variety of different devices and screen sizes.

To make sure that the site is fit for purpose, all user stories and features documented in the main README.md file will be tested. The test procedures and results are documented below.

Unit tests have also been written when required to test the individual apps.

Google Lighthouse has been used to check the Performance, Accessibility, Best Practices and Search Engine Optimisation of the website.

----------

## Responsiveness testing

### Mobile and tablet

The responsiveness of the site was tested using Device Mode in Chrome DevTools. For mobile devices the minimum screen width the site was tested at was 320 pixels.

The site was also tested on an adnroid device(huawei p30) and iad. The site was responsive across all devices and screen sizes with no unepected issues.

### Desktop

The site was tested on a desktop and a laptop using Chrome, Firefox, Edge, Opera and Safari browsers. The site was tested using the following screen widths: 1024 pixels, 1280 pixels, 1440 pixels, 1600 pixels and 1920 pixels.

---------

## User Story testing

### Feature testing

#### Navbar

The test of the navigation bar was conducted by clicking all links to check to see if they function correctly and that the correct links are displayed for admin and non admin users.

#### How i did this:

    1. Open the browser and go to: . Logout of the site if needed.
    2. Scroll down to see if the nav bar is fixed to the top of the browser window.
    3. When the user is logged out check that the following menu options appear in the My Account drop down menu:
        ◦ Register & Login
    4. Click the menu option listed above and confirm that you are taken to the correct page.
    5. Login as a regular user and make sure that the menu option My Account appears
    6. Click the menu option of my account and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the account youre logged into.
    7. Login in using an admin account and check that the following options appear in the nav bar:
        ◦ Product Management, My Profile and Logout
    8. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the account.
    9. On desktop devices confirm that clicking on the Skate Shop logo in the top left returns the user to the home page.
    10. Confirm that all the nav links under the skateboards and parts drop down menu function correctly.
    11. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
    12. Repeat the above steps using a mobile device if possible.
    13. Repeat the above tests with a screen size of <=992 pixels.

#### Register an account

This test is to confirm that user registration process works correctly.

#### How i did this:

    1. Open the browser and go to: . Logout of the site if needed.
    2. If youre logged in, then logout of the site.
    3. Click on the Register link in the menu.
    4. Confirm that the form validation functions correctly. All fields are required and the user should be prompted to complete all fields.
    Complete the form and click the Sign Up button
    5. Confirm that the user is redirected to the Verify Your Email Address page and that a message appears suggesting that a confirmation email has been sent.
    6. Confirm that a confirmation email was received at the email address used in the form.
    7. Click on the link in the confirmation email and activate the account.
    8. On the Confirm Email Address screen click on the Confirm button.
    9. Sign into the account using the user credentials that have just been confirmed.
    10. Check that the correct links appear in menu for a logged in non-admin user.
    11. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
    12. Repeat the above steps using a mobile device if possible.

#### User authentication

This test confirms that the users can log in to the site and access the pages they have permissions to view.

#### How i did this:

    1. Open the browser and go to: . Logout of the site if needed.
    2. Logout of the site if currently logged in.
    3. Then login to the site using a standard user account.
    4. Confirm that the user has access to the appropriate pages for a non admin user
    5. Logout then try the same again for an admin account.
    6. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
    7. Repeat the above steps using a mobile device if possible.

#### Log in and Sign out

This test is to confirm that the user can login and sign-out of the site and is redirected to the correct screen after sign-out.

#### How i did this:

    1. Login by clicking the login link in the menu.
    2. Logout of the account by clicking the Logout link.
    3. Confirm that the user is redirected to the Sign Out confirmation page.
    4. Click the confirm Sign Out button and check to see if the user is redirected back to the home page.
    5. Then to Confirm the correct links are displayed in the My Account dropdown menu - you should see Register and Login.
    6. Repeat the above steps using Firefox, Opera, Edge & Safari browsers.
    7. Repeat the above steps using a mobile device if possible.
    
#### Products Page

This test is to confirm that the products on the products page load correctly

#### How i did this:

    1. Access the website
    2. Go to the clothing, Skateboards and parts tabs and click all prodcuts.
    2. Repeat the first 2 steps for all options in the products section.

#### Product Details Page

This is a test to confirm that the product detail page works.

#### How i did this:

    1. Access the website
    2. Go to any products page you like
    3. Click on a product
    4. Confirm that the product details page has loaded and contains all relevant information

#### Delete and edit Products

This is to test the add and delete products part in the admin account part of the site

#### How i did this:

    1. Log in to the admin account
    2. Navigate to a products page
    3. Then find the edit and delete buttons next to each product
    4. Click on delete and delete teh product
    5. Find another product and click on edit
    6. Then edit the product and save it
    7. Go to another product and open up the product details page by clicking on the product
    8. Repeat the same process for the buttons in this part of the page as you did above

#### Delete and edit Products

This is to test the add product feature in the manage products tab in the profile section

#### How i did this:

    1. Once on the page, login as an admin
    2. Navigate to th emy profile section and then click product management
    3. Once taken to the add product page, fill out the form
    4. Click save
    5. Confirm the add product works by looking in the products page for the new product

#### Add, delete and change item numbers in the cart

This is to test adding a prodcut to the cart, deleting a product and changing the item numbers in the cart

#### To test the add to cart feature here's what i did:

    1. Go to the products page
    2. click on a product
    3. in the product details page, click add to cart
    4. confirm that hte product has entered the cart by looking in the shopping cart

#### To test the delte and change item, here is what i did:

    1. Add prodcuts to the cart by navigating to the producs page and clicking on a product, then adding it to the cart
    2. navigate to the cart at the top right of the screen
    3. click on the cart and see the shopping cart page
    4. click the increase and decrease arrows of the products in the page to see the number of products increase and decrese
    5. click the delte button and confirm 
    6. confirm that the delte item has worked by confirming that the item is no longer in the cart

#### Checkout and stripe payment

This is to test the checkout and the stripe payment function

#### How i did this:

    1. Add items to the cart from the products details page 
    2. Go to the cart
    3. Confirm youre happy with the items in your cart
    4. Click checkout
    5. Fill out the form in the checkout page
    6. Click checkout
    7. Confirm the checkout has worked by seeing the success message in the top right
    8. To confirm in greater detail, log into an admin account
    9. Navigate to the admin section by typing /admin after the webaddress
    10. Navigate to Orders
    11. View the orders in this section and confirm that it matches what you just checked out with

#### Profile Page

This test is to confirm that the profile page works as it should

#### How i did this:

    1. Log in to a user account
    2. Navigate to the profile option in the top right
    3. Confirm that youre sent to the correct page by seeing the form for your address and your order history
    4. Fill the form in and save the form, then reapeat the previous steps to check if the form has saved
    4. Repeat the same process by logging out and logging into an admin account

#### Contact Us

This is a test to confirm that the contact us form has worked correctly

#### How i did this:

    1. Navigate to the contact us page
    2. Fill in the form
    3. Click the submit button
    4. Confirm that the form has sent by looking at the top right confirmation toast

----------

## Unit tests