#에러 관리 모듈
class DownloadFailedError(Exception):
    def __str__(self):
        return '파일 다운로드에 실패했습니다.'

