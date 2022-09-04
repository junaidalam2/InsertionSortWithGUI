from tkinter import *
import random
import time


root = Tk()
root.title('Insertion Sort')
root.resizable(False, False)

array_length = 10  # number of elements in the array
lowest_number = -100  # lowest possible number of random integers
highest_number = 100  # highest possible number of random integers
animation_refresh_seconds = 0.50


frame1 = Frame(root)  # display buttons for generate array and sort
frame1.grid(row=0, column=0)

frame2 = Frame(root)  # array to be sorted
frame2.grid(row=0, column=1, sticky='n')

empty_frame3 = Frame(root, width=5)  # empty frame right of array being sorted
empty_frame3.grid(row=3, column=3, rowspan=4)


# FRAME 1: buttons to generate array and sort, and labels on time and space complexity----------------------------------

gen_num = Button(frame1, text='Generate Random Integers', fg='#2d3542', command=lambda: generate_random_array(array, index, lowest_number, highest_number, array_length))
gen_num.grid(row=0, column=0, padx=5, pady=10)

sort_num = Button(frame1, text='Sort Array', fg='#2d3542', state=DISABLED, command=lambda: sort_array(array, index))
sort_num.grid(row=1, column=0, padx=5, pady=10)

# labels describing time and space complexity
label1 = Label(frame1, text='Time Complexity:', font='Helvetica 9 bold').grid(row=3, column=0, sticky = 'w', padx=5, pady=2)
label2 = Label(frame1, text=' -Best Case: O(n)').grid(row=4, column=0, sticky = 'w', padx=5)
label3 = Label(frame1, text=' -Average Case: O(n^2)').grid(row=5, column=0, sticky = 'w', padx=5)
label4 = Label(frame1, text=' -Worst Case: O(n^2)').grid(row=6, column=0, sticky = 'w', padx=5)
label5 = Label(frame1, text='Space Complexity: O(1)', font='Helvetica 9 bold').grid(row=7, column=0, sticky = 'w', padx=5, pady=2)


# FRAME 2: array being sorted and exit button---------------------------------------------------------------------------

# array to be sorted
array = ['\0'] * array_length

# array of label names
index = [i for i in range(array_length)]

# create labels that will contain numbers being sorted
for i in range(array_length):
    height = 5
    width = 10
    index[i] = Label(frame2, text='', borderwidth=0.5, relief='sunken', bg='#add9f0', height=height, width=width)
    index[i].grid(row=0, column=i, pady=10)


# generate integers randomly
def generate_random_array(arr, index_array, low_number, high_number, arr_length):
    for i in range(arr_length):
        arr[i] = random.randint(low_number, high_number)
        index_array[i]['text'] = arr[i]

        gen_num['state'] = DISABLED
        sort_num['state'] = NORMAL


# sort array
def sort_array(arr, index_array):
    sort_num['state'] = DISABLED
    for k in range(1, len(arr)):
        i = k
        while 0 < i and arr[i - 1] > arr[i]:  # note key = array[i]
            arr[i - 1], arr[i] = arr[i], arr[i - 1]  # swap elements

            index_array[i - 1]['bg'] = '#fce803'
            index_array[i]['bg'] = '#03fc0f'

            root.update()
            time.sleep(animation_refresh_seconds)
            index_array[i - 1]['text'] = arr[i-1]
            index_array[i]['text'] = arr[i]

            root.update()
            time.sleep(animation_refresh_seconds)
            index_array[i - 1]['bg'] = '#add9f0'
            index_array[i]['bg'] = '#add9f0'

            i -= 1

    gen_num['state'] = NORMAL


# exit application
def exit_application():
    root.destroy()


empty_label1 = Label(frame2, height=5).grid(row=1, column=0)

exit_button = Button(frame2, text='Exit', command=exit_application)
exit_button.grid(row=2, column=array_length-1, sticky='se', pady=5)


root.mainloop()
