import math
import re
import requests
import nav_test
import cosine_similarity as keywordVal
import configurations
import model.pyrebase as q1
from fuzzywuzzy import fuzz

def givVal(model_answer, keywords, answer, out_of):
    
   k = keywordVal.givevalue(model_answer , answer)
   req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=JmcxHCCPZ7jfXLF6")
   no_of_errors = len(req.json()['errors'])
   print("Errors in Answer:",no_of_errors)
   if no_of_errors > 5:
        g = 0
   else:
        g = 1
   q = fuzz.token_set_ratio(keywords, answer)
   
   
   print("         Keywords : ", k)
   print("         Grammar  : ", g)
   print("         Question Related Things : ", q)
   predicted = nav_test.predict(k, g, q)
   print("_______________________________________________")

   
   return predicted[0]



firebsevar = q1.initialize_app(config=configurations.config)
db = firebsevar.database()

model_answer1 = db.child("model_answers").get().val()[1]['answer']
out_of1 = db.child("model_answers").get().val()[1]['out_of']
keywords1 = db.child("model_answers").get().val()[1]['keywords']
keywords1 = re.findall(r"[a-zA-Z]+", keywords1)

model_answer2 = db.child("model_answers").get().val()[2]['answer']
out_of2 = db.child("model_answers").get().val()[2]['out_of']
keywords2 = db.child("model_answers").get().val()[2]['keywords']
keywords2 = re.findall(r"[a-zA-Z]+", keywords2)

model_answer3 = db.child("model_answers").get().val()[3]['answer']
out_of3 = db.child("model_answers").get().val()[3]['out_of']
keywords3 = db.child("model_answers").get().val()[3]['keywords']
keywords3 = re.findall(r"[a-zA-Z]+", keywords3)



all_answers = db.child("answers").get()

for each_users_answers in all_answers.each():
    # For the first answer ->
    print("\n\n Email ID  : " + each_users_answers.val()['email'])

    answer = each_users_answers.val()['a1']
    result = givVal(model_answer1, keywords1, answer, out_of1)
   # print("Marks : " + str(result))
    #db.child("answers").child(each_users_answers.key()).update({"result1": result})

    # For the Second answer ->
    answer = each_users_answers.val()['a2']
    result = givVal(model_answer2, keywords2, answer, out_of2)
    #print("Marks : " + str(result))
    #db.child("answers").child(each_users_answers. key()).update({"result2": result})

    # For the third answer ->
    answer = each_users_answers.val()['a3']
    result = givVal(model_answer3, keywords3, answer, out_of3)
    #print("Marks : " + str(result))
    #db.child("answers").child(each_users_answers.key()).update({"result3": result})
