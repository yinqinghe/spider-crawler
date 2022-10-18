import time
from time import mktime,strptime
from File_R_W import tem_sheet,tem_wb,style,savepath
def Get_imge(re, iii, jjj):
    i = iii
    j = jjj
    picsurl = []
    items = re.get('data').get('list')
    for item in items:
        j = j + 1
        try:
            pic_infos = item.get('pic_infos')
            page_info = item.get('page_info')
            ret=item.get('retweeted_status')      #转发微博处理
            times = item.get('created_at')
            b = mktime(strptime(times, "%a %b %d %H:%M:%S +0800 %Y"))  # 将该时间格式转换成时间戳
            time1 = time.localtime(b)  # 将时间戳转换成一种特定的格式
            Etime = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            source = item.get('source')
            text = item.get('text_raw')
            message = []
            message.append(Etime)
            message.append(source)
            message.append(text)
            if pic_infos is not None:
                for p in pic_infos.values():
                    v = p.get('largest').get('url')
                    print(v)
                    i = i + 1
                    message.append(v)
                    picsurl.append(v)
            elif page_info is not None:                                          #视频链接处理
                i = i + 1
                vedio = page_info.get('media_info').get('mp4_hd_url')
                message.append(vedio)
                picsurl.append(vedio)
            elif ret is not None:
                transmit = ret.get('pic_infos')  # 转发微博   图片    处理
                media_info=ret.get('media_info')
                if transmit is not None:
                    for t in transmit.values():
                        i = i + 1
                        v0 = t.get('largest').get('url')
                        message.append(v0)
                        picsurl.append(v0)
                elif media_info is not None:
                    i = i + 1
                    ret_page_info=media_info.get('mp4_hd_url')     # 转发微博   视频    处理
                    message.append(ret_page_info)
                    picsurl.append(ret_page_info)
                else:
                    message.append("转发的一个空链接")
            else:
                message.append('链接消失的一页')
                ret=message[2].split('<a')[0]                                #解决了只有前面的数据，获取到文案   后面无信息的数据
                message[2]=ret
            # yield message
            for jj in range(0, len(message)):  # 写入数组信息
                tem_sheet.write(j, jj, message[jj], style)
            tem_wb.save(savepath)
        except:
            continue
    print("单页多条微博发布图片的总个数", i)
    print("一页获取的数据项", j)
    # f1.write(f"{nowtime}  单页多条微博发布图片的总个数:{i}\n")  # 记录运行日志
    return picsurl, i, j