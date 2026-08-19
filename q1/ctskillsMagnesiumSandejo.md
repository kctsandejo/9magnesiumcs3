# Computational Thinking Exercise
## Smart School Canteen Queue

*Name:* Kezia Cherisse
*Section:* Magnesium  
*Last Name:* Sandejo
*Date:* August 16, 2026  

---

## Step 1: Identify the Big Problem

### Main Problem
The PSHS school canteen experiences severe queue congestion and slow ordering during lunch break because the entire ordering, payment calculation, and food inventory tracking processes are handled manually without system automation or real-time tracking.

---

## Step 2: Identify the Sub-Problems

1. *Slow Order Decision-Making:* Students spend too much time viewing options and deciding what to buy while standing at the counter, delaying the line behind them.
2. *Manual Payment Calculation:* The cashier manually computes order totals and calculates change, which slows down service times and increases human error.
3. *Lack of Real-Time Food Tracking:* There is no system to track food stock levels, leading to students queuing for items that are already out of stock and unmonitored cooked food getting discarded at the end of the day.
4. *Unorganized Queue and Pickup Workflow:* There is no order status notification, causing students to crowd around the counter while waiting blindly for their orders.

---

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Slow order decision-making at the counter | Abstraction | Create a digital menu board displaying only details such as item name, price, photo, and availability status outside the queue area so students decide before lining up. |
| Manual calculation of totals and change | Algorithm Design | Create an automated system sequence that automatically monitors selected items, processes electronic or cash payment, and calculates change instantly. |
| Lack of food tracking and discarded food | Decomposition | Divide tracking into two groups: raw kitchen group and cooked display group to notify staff easily about items. |
| Unorganized queue and crowded pickup area | Pattern Recognition | Track preparation times per dish to create a sequential ticket numbers and show order status updates on a display screen. |

---

## Step 4: Algorithmic Solution

### Selected Sub-Problem
Sub-Problem 2: Manual Calculation of totals and change

### Pseudocode
## Step 4: Algorithmic Solution

### Selected Sub-Problem
Sub-Problem 2: Manual Calculation of Totals and Change (Automated Payment Processing).

### Pseudocode

START
    // Step 1: Input food details and compute total cost
        INPUT price
            INPUT qty
                SET total = price * qty
                    DISPLAY "Total Amount Due: ₱" + total

                        // Step 2: Get customer payment
                            INPUT payment

                                // Step 3: Check if payment is sufficient
                                    IF payment >= total THEN
                                            SET change = payment - total    // Automatically calculate change
                                                    DISPLAY "Payment Successful! Your change is: ₱" + change
                                                        ELSE
                                                                SET lacking = total - payment   // Automatically calculate remaining balance
                                                                        DISPLAY "Payment Failed! Additional amount needed: $" + lacking
                                                                            ENDIF
                                                                            END   
                                                                                                                                                                                                                                                                                                                                                         END
