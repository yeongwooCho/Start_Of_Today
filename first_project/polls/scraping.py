from .youtube import get_vid
from .models import Video


def scraping():
    videos1 = get_vid("공부 동기부여")
    videos2 = get_vid("취업 팁")
    videos3 = get_vid("코딩테스트")

    lis = [videos1, videos2, videos3]
    for li in lis:
        for data in li:
            video = Video(
                num=data['num'],
                title=data['title'],
                views=data['views'],
                url=data['url'],
            )
            if not Video.objects.filter(title=video.title):
                video.save()


if __name__ == "__main__":
    scraping()
