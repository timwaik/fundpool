"""This is an attempt to create a money management system. Similar to splitwise,
but in a reverse manner, it holds money each individual pools into a mutual fund.
When expenses are paid out, the app will substract the amount contributed by each
user accordingly.

However, individual users have the option of not paying for
certain expenses. Thus an equal amount will be deducted from each contributing
user, leaving out the users who have not contributed. Users will then be able
to view the remaining balance from each user. This eliminates the need for
multiple groups for users who want to share different things, when users can just
opt out of the payment."""

class User(object):
    """docstring for User."""
    user_count = 0

    def __init__(self, balance):
        super(User, self).__init__()
        self.balance = balance
        self.user_id = User.user_count
        User.user_count += 1
        self.groups = []

    def substract(self, deduction):
        self.balance -= deduction

    def addition(self, addition):
        self.balance += addition

    def view_balance(self):
        return self.balance
