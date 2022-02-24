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

#### How i did this:

#### Product Details Page

#### How i did this:

#### Sorting Categories and Search

#### How i did this:

#### Add and delete Products

#### How i did this:

#### Edit Products

#### How i did this:

#### Add, delete and change item numbers in the cart

#### How i did this:

#### Checkout and stripe payment

#### How i did this:

#### Profile Page

#### How i did this:

#### Contact Us

#### How i did this:

----------

## Unit tests