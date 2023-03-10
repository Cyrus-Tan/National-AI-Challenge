# National-AI-Challenge
<h1> Project's Title: Home Groceries Inventory Tracker </h1>

<h1> Project's Description </h1>
In Singapore, there is a huge issue of food waste with 26,000 tonnes of food being thrown out by households yearly. A study done by Electrolux found that about 48% of Singaporeans are guilty of throwing out forgotten or expired food, making expired food one of the largest contributors to food wastage. The main cause of this is that people often forget what they buy when they go grocery shopping. Our software is expected to help users track whether a grocery item exists currently in their home, how much they have, and their expected date of expiry. This will help them keep track and not overbuy on grocery items.

<h2> Idea </h2>
<h3> 1: Using PeekingDuck, the software will identify whether the image is a receipt. </h3>
<h3> 2: We will then use OpenCV for image processing, which will read the contents of the receipt into a text file. </h3>
<h3> 3: We use ScikitLearn to categorise the grocery items in a supermarket. </h3>
<h3> 4: The contents of the text file will then be compared against the database of grocery items from a supermarket (e.g: NTUC FairPrice). </h3>
<h3> 5: Items in the supermarket will be identified as comsumables when there is an expiry date tagged to the item in the database. </h3>
<h3> 6: The app will keep track of the type, quantity, expiry date of the consumables each user have in his/her database. </h3>
<h3> 7: Users are expected to manually 'delete' an item from the app when they have finished consuming it. </h3>

<h2> Challenges </h2>
<ol> 
  <li> When scanning a receipt, the receipt may be creased/not taken at a top-down clear angle. As such, contents of the receipt may not be identifiable. In future, we plan to leverage on page dewarping to flatten images of curled pages, improve optimisation.</li>
  <li> Users of the app are expected to manually remove the consumable items in the app once they have finished consuming it at home. However, if users forget to update the quantity in the app, this will lead to inaccurate representation of the quantity of the item in the app. </li>
  <li> With a lack of data to train the model, the categorisation process of the model is slightly innaccurate </li>
</ol>

<h2> Languages and Library used </h2>
<ol> 
  <li> Python </li> 
  <li> PeekingDuck </li>
  <li> OpenCV </li>
  <li> Pytesseract </li>
  <li> ScikitLearn </li>
</ol>
