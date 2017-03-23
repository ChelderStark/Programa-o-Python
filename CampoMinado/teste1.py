import pickle
import os

'''file = open('salvo.pkl', 'rb')
a = pickle.load(file)
print(a)
'''

if os.path.exists('salvo.pkl') == True:
    print("Existe")
    current_directory = os.getcwd()
    print(current_directory)
    os.unlink('salvo.pkl')
