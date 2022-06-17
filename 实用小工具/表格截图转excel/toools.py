from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

import base64
import cv2


def img_to_excel(output_filename, img_path, secret_id, secret_key):
    # 实例化一个认证对象
    cred = credential.Credential(
        secret_id,
        secret_key
    )

    # 实例化client对象
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

    # 实例化一个请求对象
    req = models.RecognizeTableOCRRequest()

    # 读取图片使用base64编码
    with open(img_path, 'rb') as f:
        imge = f.read()
        imge_base64 = str(base64.b64encode(imge), encoding='utf-8')

    req.ImageBase64 = imge_base64

    # 通过client对象调用接口
    resp = client.RecognizeTableOCR(req)

    # 获取返回后的数据（data为base64编码的excel数据）
    data = resp.Data

    # 保存为excel文件
    output_filename = str(output_filename)
    path_excel = output_filename + ".xlsx"
    with open(path_excel, 'wb') as f:
        f.write(base64.b64decode(data))

    return path_excel


def cut_pic(img_path):
    src = cv2.imread(img_path)
    img_list = []

    if src.shape[0] > 5000:
        sub_image_num = src.shape[0] // 5000

        sub_images = []
        src_height, src_width = src.shape[0], src.shape[1]
        sub_height = src_height // sub_image_num

        for i in range(sub_image_num):
            image_roi = src[i * sub_height: (i + 1) * sub_height, :, :]
            sub_images.append(image_roi)

        for i, img in enumerate(sub_images):
            cv2.imwrite('sub_img_' + str(i) + '.png', img)
            img_list.append('sub_img_' + str(i) + '.png')
    else:
        img_list.append(img_path)

    return img_list
