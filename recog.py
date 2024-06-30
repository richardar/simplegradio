from deepface import DeepFace


def compare(img1,img2):

    return DeepFace.verify(
    img1_path = img1,
    img2_path = img2,
    )
