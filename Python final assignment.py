#1
feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}
#2
f=int(input("How many more feedbacks you want to add:"))
for i in range (1,f+1):
    name=input("Enter name:")
    feedback=input("Your feedback here:")
    rating=int(input("Your rating pls:"))
    feedback_data['S_No'].append(10+i)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)
print(feedback_data)
#3
for i in range(len(feedback_data['Feedback'])):
    feedback = feedback_data['Feedback'][i]
    feedback = feedback.replace(".", "")
    feedback = feedback.replace(",", "")
    feedback = feedback.replace("!", "")
    feedback = feedback.replace("?", "")
    feedback = " ".join(feedback.split())
    feedback = feedback.lower()
    feedback_data['Feedback'][i] = feedback
print(feedback_data['Feedback'])
#4
def count_word_in_feedbacks(word):
    count=0
    for i in range(len(feedback_data['Feedback'])):
        if word.lower() in feedback_data['Feedback'][i].lower():
            count+=1
    return count
print(count_word_in_feedbacks("good"))
print(count_word_in_feedbacks("poor"))
print(count_word_in_feedbacks("excellent"))
#5
print("Cleaned data")
print(feedback_data)
Avgrating=sum(feedback_data['Rating'])/len(feedback_data['Rating'])
print(Avgrating)
longest_feedback = ""
max_words = 0
for feedback in feedback_data['Feedback']:
    word_count = len(feedback.split())
    if word_count > max_words:
        max_words = word_count
        longest_feedback = feedback
print("Longest feedback:", longest_feedback)
print("Word count:", max_words)
unique_words = set()
for feedback in feedback_data['Feedback']:
    words = feedback.split()
    for word in words:
        unique_words.add(word)
print("Unique words:")
print(unique_words)
sorted_data = list(zip(
    feedback_data['S_No'],
    feedback_data['Name'],
    feedback_data['Feedback'],
    feedback_data['Rating']
))
sorted_data = sorted(sorted_data, key=lambda x: x[3], reverse=True)
print("\nFeedbacks sorted by rating:")
for entry in sorted_data:
    print(entry)


