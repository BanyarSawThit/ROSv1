# dining session

* objective 3
* est. time - 1 day (feb 7 - feb )
* actual time - 

Next I wanna focus on dining session. 

Right now, different devices can access order history of a table.
Various customers can see the same order history in a table, that's intended.
But when a table is paid and closed. Next customers shouldn't be able to access that. 

So solution is we add 'dining session' to table model. 
this model will have 
1. active field
2. created/close time
I'm not sure about created time. but close time or paid time and is_active are a must right.

From now on, I'll keep track of how i'm doing my projects as a note in the projects.
Adding notes and comments on how i'm doing, where i'm going and how well did i do to evaluate.


things to work on:
1. add DiningSession to table
2. add that to views
3. wire with urls to templates

Customer POV
Scan qr -> Welcome page -> browse menu -> add to cart -> confirm order

Background?
QR scanned -> welcome page 
- start dining session
once paid
- end dining session

1. created DiningSession model 
2. added as foreign key to Table, and Order model
3. created a dining_session in the Table views.start()
4. end when a payment is made. (later in payment app)
5. Cart_details also needed to be secured.

Next objectives:
1. add welcome page when qr scan
2. add payment