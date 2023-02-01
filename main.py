#1
def upper(N):
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z']

    count_up = 0
    for i in N:
        if i in upper:
            count_up += 1
    return count_up
print(upper("ME mqvia NinI"))

# შედარებები ხდება ასოების მიხედვით, რადგან ვეძებთ დიდი ასოების მიხედვით, საუკეთესო შემთხვევა იქნება,
# როცა არცერთი დიდი ასო არ შეგვხვდება და მოხდება 0 მინიჭება,
# ხოლო უარესი შემთხვევაა, როცა მთლიანად დიდი ასოებითა ჩაწერილი, ანუ რაოდებობა დიდი ასოების ანუ count_up

#2
def avg(set):
    sum = 0
    quantity = 0
    for i in set:
        sum = sum + i
        quantity += 1
    avg = sum / quantity
    return avg
print(avg([1, 5, 3]))

# მინიჭებების რაოდენობა არის იმდენი, რამდენი რიცხვიც გვაქვს, ანუ N რაოდენობა


#3
def compression(a, b, c):
    if a != b:
        if a != c:
            if b != c:
                return "განსხვავებულია"
            return "ყველა განსხვავებული არ არის"
        return "ყველა განსხვავებული არ არის"
    return "ყველა განსხვავებული არ არის"
print(compression(3,3,1))

# საშუალო შედარებების რაოდებობა არის 2
# 1* 1/3 + 2 * 1/3 + 3 * 1/3 = 2

#4
def max_find(a, b, c):
    if a > b and a > c :
        return a
    elif b > a and b > c:
        return b
    else: return c

print(max_find(1,5,20))
# როცა a არის უდიდესი მოხდება 2 შედარება და ეს არის საუკეთესო შემთხვევა, უარესი შემთხვევის დროს ხდება 4 შედარფება



#5
def sec_largest(array):
    largest = array[0]
    for i in range(1, len(array)):
        if array[i] > largest:
            largest = array[i]

    sec_largest = array[0]
    index = 0
    for i in range(1, len(array)):
        if array[i] > sec_largest and array[i] != largest:
            sec_largest = array[i]
            index = i
    return index

print(sec_largest([-6, 5, 0, 100, 555]))
