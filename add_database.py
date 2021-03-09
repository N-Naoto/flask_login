from models.database import db_session
from models.models import OnegaiContent

# c1 = OnegaiContent('おねがい1','内定をください')
# c2 = OnegaiContent('おねがい2','お金がほしい')
# c3 = OnegaiContent('おねがい3','ケーキが食べたい')
# c4 = OnegaiContent('おねがい4', '頭がよくなりますように')

# db_session.add(c1)
# db_session.add(c2)
# db_session.add(c3)
# db_session.add(c4)
db_session.commit()
