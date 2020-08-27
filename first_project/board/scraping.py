from .pusan_cse import get_notices
from .pusan_info import get_busanits
from .pusan_jobs import get_emps
from .pusan_Smart import get_smarts
from .views import Board


def scraping():
    pusanits = get_busanits()
    notices = get_notices()
    emps = get_emps()
    smarts = get_smarts()
    # {'scp_notices': notices, 'scp_pusanits': pusanits, 'scp_emps': emps, 'scp_smarts': smarts}
    lis = [pusanits, notices, emps, smarts]
    for li in lis:
        for data in li:
            board = Board(
                num=data['num'],
                title=data['title'],
                rate=data['rate'],
                link=data['link'],
            )
            if not Board.objects.filter(title=board.title):
                board.save()

    # post_instance = Post.objects.get(id=66)
    # post_instance.delete()


if __name__ == '__main__':
    scraping()
