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