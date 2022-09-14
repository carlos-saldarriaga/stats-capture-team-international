from app.data_capture import DataCapture


def main():
    capture = DataCapture()

    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)


    stats = capture.build_stats() 

    print('Less than 4: ', stats.less(4))
    print('Grater than 4: ', stats.greater(4))
    print('Bewtween  4 and 6: ', stats.between(3,6))

if __name__ == "__main__":
    main()