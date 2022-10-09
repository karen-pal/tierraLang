def s(a): 
    b = a.replace(" ","_").replace(";","") 
    print("mv '"+a+"' "+b) 
    print() 
    print("scp kpalacio@nabucodonosor.ccad.unc.edu.ar:/users/kpalacio/notebook/content/video/"+b+ " ./")                                                                                                                                                                            
    print() 
    reverse = "ffmpeg -i " + b + " -vf reverse "+ b.split(".")[0] + "_reversed.mp4"
    print(reverse)


