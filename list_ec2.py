import boto3

def list_all_ec2_instances():
    """
    내 AWS 계정의 모든 EC2 인스턴스 정보(ID, 상태)를 출력합니다.
    """
    try:
        # ec2 서비스를 사용 선언
        ec2_client = boto3.client('ec2')
        
        # EC2 인스턴스 정보 요청
        response = ec2_client.describe_instances()
        
        print("--- EC2 인스턴스 목록 ---")
        
        # response에서 정보 추출
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                
                print(f"  [ID]: {instance_id}, [상태]: {instance_state}")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")

# 이 스크립트가 직접 실행될 때만 함수 호출
if __name__ == "__main__":
    list_all_ec2_instances()