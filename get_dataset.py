import os

# ================= 配置区域 =================
# 1. 指向你存放图片的【绝对路径】或【相对路径】
dataset_path = '/kaggle/working/esod/'
# 2. 训练集和验证集的文件夹名称
train_folder = 'images/train'
val_folder = 'images/val'
# 3. 输出的文本文件名
train_out = 'train.txt'
val_out = 'val.txt'


# ===========================================

def generate_list(folder, output_file):
    target_dir = os.path.join(dataset_path, folder)
    if not os.path.exists(target_dir):
        print(f"警告: 找不到文件夹 {target_dir}")
        return

    # 获取所有图片文件（支持 jpg, jpeg, png, bmp）
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    files = [os.path.join(target_dir, f) for f in os.listdir(target_dir) if f.lower().endswith(valid_extensions)]

    with open(output_file, 'w') as f:
        for file_path in files:
            # 写入绝对路径，这样不管你在哪运行训练脚本都能找到图
            f.write(os.path.abspath(file_path) + '\n')

    print(f"成功生成 {output_file}，共 {len(files)} 张图片。")


if __name__ == "__main__":
    generate_list(train_folder, train_out)
    generate_list(val_folder, val_out)