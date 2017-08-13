from application import db

db.create_all()

def put_initial_value():
    import application.models as model
    targets = [
    model.Target('lover', name_kor='연인')
    ,model.Target(name='soldier', name_kor='군인')
    ,model.Target('parents', name_kor='부모님')
    ]

    recommendations =[
    model.Recommendation('우산이 있는데 비를...', image_url=r'http://t1.daumcdn.net/liveboard/movie/f6c5a1895b9642e19421890ee8557734.jpg', target=targets[0], upvotes=10)
    ,model.Recommendation('그대와 함께한 모든 날이 좋았다.', image_url=r'http://mblogthumb3.phinf.naver.net/MjAxNzAxMDVfMjkg/MDAxNDgzNjEyNDg2NTEy.DsQKi_x9LF_Bal-kXtgoe11MrrQ94FhQmtXC60UUdrEg.hBGWVdeZm4h-hJznMCECIOUmPiZYFx1_bmQFYLXgHMUg.JPEG.bihangsonyu/%EB%8F%84%EA%B9%A8%EB%B9%84%2C%EB%8F%84%EA%B9%A8%EB%B9%84%EB%AA%85%EB%8C%80%EC%82%AC%2C%EA%B3%B5%EC%9C%A0%2C%EB%8F%84%EA%B9%A8%EB%B9%84%EA%B3%B5%EC%9C%A0%2C%EB%93%9C%EB%9D%BC%EB%A7%88%EB%8F%84%EA%B9%A8%EB%B9%84%2C%EB%8F%84%EA%B9%A8%EB%B9%84%EA%B9%80.jpg?type=w800', target=targets[0], upvotes=25)
    ,model.Recommendation('조국이 당신을 원한다!', targets[1], r'https://image.webtoonguide.com/xe/attach/images/3199/350/008/b32c7564bc8c5929674a555584c04c0b.jpg', 12)
    ,model.Recommendation('엄마 없는 하늘 아래', targets[1], r'http://cfile10.uf.tistory.com/image/21108C3852312B371C9174', 14)
    ,model.Recommendation('다행', targets[2], r'http://www.insightofgscaltex.com/wp-content/uploads/2014/12/%EA%B5%AD%EC%A0%9C%EC%8B%9C%EC%9E%A5-%EB%AA%85%EB%8C%80%EC%82%AC.png', 13)
    ,model.Recommendation('자식', targets[2], r'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQG8f1DUdnxc_zKYlaNV8FxeIH5QE2FXcwQjjohNjn5SRTKotqn', 20)
    ]
    for target in targets:
        model.db.session.add(target)
    for recommendation in recommendations:
        model.db.session.add(recommendation)

    model.db.session.commit()

put_initial_value()
