import pickle
f = open('setting.txt', 'wb')
setting = [{'title': 'python program'}, {'author': 'kei'}]
pickle.dump(setting, f)
f.close()
