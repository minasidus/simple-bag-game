
import random
import cv2
counter=1
bag1=10
bag2=10
bag3=10
x=0
while bag1>0 or bag2>0 or bag3>0:

    while counter%2!=0:

        counter=counter+1
        user_bag=int(input("please enter your bag nb"))
        user_input=int(input("please enter nb of items"))
        if user_input>0 and user_input<6:
            if user_bag<4 and user_bag>0:
                if user_bag==1:
                    if bag1>0 and bag1 - user_input>=0:
                        bag1 = bag1 - user_input
                        print("you took"+str(user_input)+"from"+str(user_bag))
                        if bag1 == 0 and bag2 == 0 and bag3 == 0:
                            print("you won")
                            photo = cv2.imread("youwin (1).jpg")
                            cv2.imshow("you win", photo)
                            cv2.waitKey(0)

                        else:
                            print(bag1)
                            print(bag2)
                            print(bag3)
                    else:
                        print("please choose another bag than bag1")
                        counter=counter-1

                elif user_bag ==2:
                    if bag2 > 0  and bag2 - user_input>=0:
                        bag2 = bag2 - user_input
                        print("you took" + str(user_input) + "from" + str(user_bag))
                        if bag1 == 0 and bag2 == 0 and bag3 == 0:
                            print("you won")
                            photo = cv2.imread("youwin (1).jpg")
                            cv2.imshow("you win", photo)
                            cv2.waitKey(0)
                        else:
                            print(bag1)
                            print(bag2)
                            print(bag3)
                    else:
                        print("please choose another bag than bag2")
                        counter=counter-1

                elif user_bag==3:
                    if bag3 >= 0 and bag3 - user_input>=0:
                        bag3 = bag3 - user_input
                        print("you took" + str(user_input) + "from" + str(user_bag))
                        if bag1 == 0 and bag2 == 0 and bag3 == 0:
                            print("you won")
                            photo = cv2.imread("youwin (1).jpg")
                            cv2.imshow("you win", photo)
                            cv2.waitKey(0)
                        else:
                            print(bag1)
                            print(bag2)
                            print(bag3)
                    else:
                        print("please choose another bag than bag3")
                        counter=counter-1

            else:
                print("please enter a nb between 1 and 3")

        else:
            print("enter a valid nb")

    while counter % 2 == 0:
        if user_bag<4 and user_bag>0 and user_input>0 and user_input<6:
            pc_bag=random.randint(1,3)
            pc_input=random.randint(1,5)
            if pc_bag==1:
                if bag1>0 and bag1-pc_input>=0 :
                    bag1=bag1-pc_input
                    print("computer took" + str(pc_input) + "from" + str(pc_bag))
                    if bag1 == 0 and bag2 == 0 and bag3 == 0:
                        print("you lost")
                        photo = cv2.imread("sorryyoulost.jpg")
                        cv2.imshow("sorry", photo)
                        cv2.waitKey(0)
                    else:
                        print(bag1)
                        print(bag2)
                        print(bag3)
                else:
                    counter=counter-1
            if pc_bag == 2:
                if bag2 > 0 and bag2 - pc_input>=0:
                    bag2 = bag2 - pc_input
                    print("computer took" + str(pc_input) + "from" + str(pc_bag))
                    if bag1 == 0 and bag2 == 0 and bag3 == 0:
                        print("you lost")
                        photo = cv2.imread("sorryyoulost.jpg")
                        cv2.imshow("sorry", photo)
                        cv2.waitKey(0)
                    else:
                        print(bag1)
                        print(bag2)
                        print(bag3)
                else:
                    counter = counter-1

            if pc_bag == 3:
                if bag3 > 0 and bag3 - pc_input >=0 :
                    bag3 = bag3 - pc_input
                    print("computer took" + str(pc_input) + "from" + str(pc_bag))
                    if bag1 == 0 and bag2 == 0 and bag3 == 0:
                        print("you lost")
                        photo = cv2.imread("sorryyoulost.jpg")
                        cv2.imshow("sorry", photo)
                        cv2.waitKey(0)
                    else:
                        print(bag1)
                        print(bag2)
                        print(bag3)
                else:
                    counter=counter-1

        counter=counter+1













