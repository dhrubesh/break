import webbrowser
import time
total_breaks=3
break_count=0
print("the program started on "+ time.ctime())
while(break_count<total_breaks):
        time.sleep(2)
        webbrowser.open("https://www.youtube.com/watch?v=2OpCAiBAlpo")
        break_count+=1
