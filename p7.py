def konversiSuhu(C = "none", F = "none"):
           "mengkonversikan suhu dari celcius ke Farenheit atau sebaliknya"
           suhu = 0
           if (C == "none") and (F == "none"):
               print ("Suhu 0 Celcius setara dengan 32 Farenheit")
           elif (C == "none") and (F == "none"):
              suhu = (F - 32) * 5/9
              print "Suhu", F, "Farenheit setara dengan", int(suhu), "Celcius"
           elif (C != "none") and (F == "none"):
               suhu = (C * 9/5) + 32
               print "Suhu", C, "Celcius setara dengan", int(suhu), "Farenheit"
           
