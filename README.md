# Sports or Comedy Preference Quiz

## Purpose
This is a fun, interactive Python program that helps users determine whether they prefer watching sports or comedy, and within those categories, which specific interests they align with. The program takes user input and responds based on the choices, either assigning a sport or a comedy actor based on their answers.

## How It Works
The program asks the user a series of questions based on their initial choice of sports or comedy. Depending on their responses, the program narrows down their preferences, either by determining their favorite sport (basketball or football) or their favorite comedian (Tom Cruise or Jim Carrey). The logic works as follows:

1. Do you prefer to watch sports or comedy?
   - If sports, the program asks about basketball or football.
   - If comedy, the program asks about Tom Cruise or Jim Carrey.

2. Do you prefer to watch basketball or football?
   - If basketball, the user is assumed to be a basketball fan.
   - If football, the user is assumed to be a football fan.

3. Do you prefer to watch Tom Cruise or Jim Carrey?
   - If Jim Carrey, the user is assumed to like comedy.
   - If Tom Cruise, the program concludes the user prefers more serious action over comedy.

## Code Explanation
1. Input Gathering:
   The program asks the user about their preference between sports and comedy and stores their answers in variables (`favoriteShow`, `favoriteSport`, `favoriteActor`).

2. Conditional Logic:
   The program uses `if-else` statements to check the answers. Depending on the user's responses, it prints a tailored message that matches their choices.

3. Output:
   Based on the user's input, the program outputs a personalized response about their sports or comedy preferences.

## Example Output

```plaintext
sports or comedy?
_______________
Do you prefer to watch sports or comedy? sports
So you must like the competitive scene!
Do you prefer to watch basketball or football? football
You must be a football fan!
