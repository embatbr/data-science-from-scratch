"""Code from the chapter 1, Introduction.
"""


def add_friends_to_all_users(users, friendships):
    for user in users:
        user['friends'] = list()

    for (i, j) in friendships:
        users[i]['friends'].append(users[j])
        users[j]['friends'].append(users[i])

num_friends = lambda user: len(user['friends'])
num_connections = lambda users: sum([num_friends(user) for user in users])


if __name__ == '__main__':
    users = [
        { 'id': 0, 'name': 'Hero' },
        { 'id': 1, 'name': 'Dunn' },
        { 'id': 2, 'name': 'Sue' },
        { 'id': 3, 'name': 'Chi' },
        { 'id': 4, 'name': 'Thor' },
        { 'id': 5, 'name': 'Clive' },
        { 'id': 6, 'name': 'Hicks' },
        { 'id': 7, 'name': 'Devin' },
        { 'id': 8, 'name': 'Kate' },
        { 'id': 9, 'name': 'Klein' }
    ]

    friendships = [
        (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7),
        (6, 8), (7, 8), (8, 9)
    ]

    add_friends_to_all_users(users, friendships)

    avg_num_connections = num_connections(users) / len(users)
    print(avg_num_connections)

    num_friends_by_user = [(user['name'], num_friends(user)) for user in users]
    ranking = sorted(num_friends_by_user, key=lambda t: t[1], reverse=True)
    print(ranking)
