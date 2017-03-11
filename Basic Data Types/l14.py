if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    score_query = student_marks[query_name]
    avg = (score_query[0]+score_query[1]+score_query[2])/3
    print("%.2f" % avg )
