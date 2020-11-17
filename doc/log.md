# データドリブンの課題のためのやつ

## Logger(dir)
___
An interface for managing user logs from User object

### Logger.**logs**
*dict* Raw logs for every user. 
#
    {
        'User1': [
            (date1, steps1),
            (date2, steps2),
            ...
        ],
        'User2': [
            (date1, steps1),
            (date2, steps2),
            ...
        ],
        ...
    }
### Logger.**users**
