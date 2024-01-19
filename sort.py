def bubble_sort(score, numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range (0, len(score)-1):
            if score[i] > score[i + 1]:
                temp = score[i]
                score[i] = score[i + 1]
                score[i + 1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

              
scores = [60, 50, 60, 58, 54, 54,
58, 50, 52, 54, 48, 69,
34, 55, 51, 52, 44, 51,
69, 64, 66, 55, 52, 61,
46, 31, 57, 52, 44, 18,
41, 53, 55, 61, 51, 44]

number_of_scores = len(scores)
solution_number = list(range(number_of_scores))  

bubble_sort(scores, solution_number)
print(scores)

print('Top Bubble Solution')
for i in range(0, 5):
  print(str(i+1) + ')',
         print('Bubble solution #' + str(solution_number[i])),
         'score:', scores[i])
         
 
         








