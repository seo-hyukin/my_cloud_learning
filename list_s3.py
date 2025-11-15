import boto3

def list_all_s3_buckets():
    """
    내 AWS 계정의 모든 S3 버킷 목록(이름, 생성일)을 출력합니다.
    """
    try:
        # s3 서비스를 사용 선언
        s3_client = boto3.client('s3')
        
        # S3 버킷 목록을 'list_buckets'로 요청
        response = s3_client.list_buckets()
        
        print("--- S3 버킷 목록 ---")
        
        # response에서 'Buckets' 리스트를 순회
        if 'Buckets' in response and response['Buckets']:
            for bucket in response['Buckets']:
                # 4. 필요한 정보(이름, 생성일)만 추출
                bucket_name = bucket['Name']
                creation_date = bucket['CreationDate']
                
                print(f"  [이름]: {bucket_name}, [생성일]: {creation_date}")
        else:
            print("  (생성된 S3 버킷이 없습니다.)")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

# 이 스크립트가 직접 실행될 때만 함수 호출
if __name__ == "__main__":
    list_all_s3_buckets()