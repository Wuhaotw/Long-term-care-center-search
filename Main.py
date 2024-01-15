if __name__ == "__main__":    
    import tkinter as tk
    from tkinter import ttk

    # 視窗
    root = tk.Tk()
    root.title("老人長期照護中心")
    root.geometry("1366x768")


    # 縣市
    counties = ["台北市","新北市"]
    canvas1 = tk.Canvas(root, width=1366, height=768)
    canvas1.pack()


    # 第一頁背景
    bg_img = tk.PhotoImage(file='3230e954ee3fc092.png')
    bg_img_item = canvas1.create_image(0, 0, image=bg_img, anchor='nw')


    #第二頁設定
    def goto_page2(center_name=None):
        if center_name:
            canvas_pages[center_name].pack_forget()

        canvas1.pack_forget()  # 隱藏第一頁
        canvas2.pack()  # 顯示第二頁
        label_page2.pack()
        county_combobox.pack()
        button_page2.pack(side=tk.BOTTOM)
        canvas2.configure(width=1366, height=768)  

    # 前往第二頁按鈕
    button_page1 = tk.Button(canvas1, text='點擊繼續', command=goto_page2,font=("Arial", 18))
    canvas1.create_window(485, 560, height=70, width=280, anchor='nw', window=button_page1)  # Button



    # 第二頁視窗
    canvas2 = tk.Canvas(root, width=1366, height=768)
    canvas2.pack_forget()

    # 第二頁選單
    label_page2 = ttk.Label(canvas2, text="請選擇縣市", font=("華文細黑", 24))
    label_page2.pack(pady=20)

    county_combobox = ttk.Combobox(canvas2, values=counties, font=("Arial", 18),state="readonly")
    county_combobox.pack()

    # 縣市選擇確定紐
    button_page2 = tk.Button(canvas2, text="確定", command=lambda: show_selected(county_combobox.get()),height=1, width=8,font=("Arial", 18))
    button_page2.pack(side=tk.BOTTOM)

    def show_selected(selected_county):
        result = ""

        # 清除先前的列表
        for widget in canvas2.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()
    
        #長照中心連結
        if selected_county in data:
            centers = data[selected_county]
            for center in centers:
                result += f"{center}\n"
                center_name = center
                center_content = content_data.get(center_name, "")
                link_label = tk.Label(canvas2, text=center, fg="blue", cursor="hand2", font=("Arial", 18))
                link_label.pack()
                link_label.bind("<Button-1>", lambda e, name=center_name: open_link(name))

        button_page2.pack(side=tk.BOTTOM)
        canvas2.configure(width=1366, height=768)

    # 長照中心的分頁
    canvas_pages = {}
    def open_link(center_name):
        #隱藏第二頁
        canvas2.pack_forget()

    #創建長照中心的分頁
        if center_name not in canvas_pages:
            canvas = tk.Canvas(root, width=1366, height=768)
            canvas.pack()

            # 分頁標題
            label_name = tk.Label(canvas, text=center_name, font=("Arial", 24, "bold"), padx=20, pady=10)
            label_name.pack()

            # 長照中心內容字體
            center_content = content_data.get(center_name, {}).get("text", "")
            label_content = tk.Label(canvas, text=center_content, font=("Arial", 14), padx=20, pady=10, wraplength=500)
            label_content.pack()

            # 分頁圖片
            image_path = content_data.get(center_name, {}).get("image_path")
            if image_path:
                img = tk.PhotoImage(file=image_path)
                img_label = tk.Label(canvas, image=img)
                img_label.image = img
                img_label.pack()
            
            # 返回第二頁
            button_back = tk.Button(canvas, text="返回", command=lambda name=center_name: goto_page2(center_name),width=10, height=2)
            button_back.pack(pady=10)

            # 儲存分頁
            canvas_pages[center_name] = canvas
        else:
            canvas_pages[center_name].pack()

    # 長照中心的資料內容
    content_data = {
        "臺北市至善老人安養護中心": {
            "text": "臺北市政府社會局為推動優質之長者照護服務，並落實「就地安老」及「照護社區化」之政策，提供環境優美、設計完善的多層次安養護型式的至善老人安養護中心，委託民間經營管理。\n\n聯絡電話：02—28832666\n地址: 士林區仰德大道二段2巷50號",
            "image_path": "t1.png",

        },
        "臺北市私立永青老人長期照顧中心": { 
            "text": "台北市私立永青老人長期照顧中心，本中心對於傷口照護、營養調理、失能照護，都有豐富的經驗，能協助長者縮短恢復期!為全身或半身癱瘓、長期慢性病、失能、失智、氣切、造口、洗腎的長輩，提供一個可以安心休養、放心調理、靜心生活的好環境!\n\n聯絡電話:0912-202-681\n地址:士林區中山北路六段427巷8號",
            "image_path": "t2.png",
        },
        "臺北市私立天玉老人長期照顧中心": {
            "text": "提供24小時多元專業照護盼能陪伴失能者提升生命品質而非專注於生命延長\n\n聯絡電話:02-2872-0239\n地址:士林區天玉街38巷18弄18號",
            "image_path": "t3.png",
        },
        "臺北市私立健全老人長期照顧中心":{
            "text": "聯絡電話:02-2394-3266\n地址:金山南路二段152號2-6樓",
            "image_path": "t4.png",

        },
        "臺北市兆如老人安養護中心":{
            "text": "臺北市兆如老人安養護中心於1999年4月由臺北市政府籌建完成，2001年10月以公設民營模式委託『財團法人臺北市私立恆安老人長期照顧中心(長期照護型)』經營管理，提供老人全方位照顧服務。\n\n聯絡電話:02-8661-2410\n地址:文山區政大二街129號",
            "image_path": "t5.png",

        },
        "臺北市私立恆安老人長期照顧中心":{
            "text": "我們以「安全、尊嚴、充實、快樂」的核心價值，讓長者獲致溫馨的頤養生活。\n\n聯絡電話:02-2332-7973\n地址:萬華區水源路187號",
            "image_path": "t6.png",

        },
        "臺北市私立華安老人長期照護中心":{
            "text":"聯絡電話:02-2771-7172\n地址:大安區華聲里007鄰光復南路116巷1、3、5號5樓及3號6樓",
            "image_path": "t7.png",
        },
        "臺北市私立全民老人長期照顧中心":{
            "text":"聯絡電話:02-2876-1692\n地址:北投區永欣里013鄰石牌路2段317號1~2樓",
            "image_path":"t8.png",
        },
        "臺北市私立安安老人長期照顧中心":{
            "text" : "秉持有感覺之服務精神，以照顧行動不便的老人，提供無微不至的生活照顧為原則，讓住民在本院也能擁有像在家一樣的感覺，以事業化及人性化的照顧，提供24小時的全天服務，我們以耐心服務的工作精神，結合居家護理及醫療支援服務，落實了本機構之服務宗旨：將心比心，待老猶親。\n\n聯絡電話:02-2895-3298\n地址:北投區公舘路194號",
            "image_path" : "t9.png",

        },
        "財團法人台灣省私立健順養護中心":{
            "text": "健順提供了一個健康、順心如意的家。\n\n聯絡電話:02-2662-2499\n地址:深坑區昇高里王軍寮九號",
            "image_path": "n1.png",

        },
        "新北市私立銀泰老人長期照顧中心":{
            "text": "以「優質照護、教學相長」服務態度來照顧需長期照顧的個案，秉持以人為本、家庭為中心的思維，發揮3C精神：照護(care)、 關懷(concern)、 悲憫(compassion)的心與積極創新的服務精神，提昇住民的獨立性、減緩老化，使其其身體、智能、情緒及靈性上能發揮最大的功能。\n\n聯絡電話:02-2693-4386\n地址:汐止區福德路38號6樓之1~6",
            "image_path": "n2.png",

        },
        "新北市私立心田老人長期照顧中心":{
            "text": "秉持有家的感覺之服務精神，以照顧行動不便之長者提供無為不至的生活照顧為原則讓原住民在本所也能擁有像在家一樣的感覺。故本所成立目的旨在使居住本所的長者不僅達成長老有所終的目的，更使老人在有家人、朋友、工作人員的陪伴下有快樂和充實的晚年生活。\n\n聯絡電話:02-8951-1426\n地址:板橋區廣權路2號",
            "image_path": "n3.png",

        },
        "新北市私立夏雨老人長期照顧中心":{
            "text": "以專業知能為每位住民提供人性化與有尊嚴之關懷照顧，我們願意盡力使住民有健康、快樂、幸福的生活。\n\n聯絡電話:02-2600-0888\n地址:林口區三民路75號",
            "image_path": "n4.png",

        },
        "財團法人私立廣恩老人養護中心":{
            "text": "廣恩老人養護中心，提供住民全方位的照護服務。\n\n聯絡電話:02-2217-6699\n地址:新店區北宜路二段579巷45號",
            "image_path": "n5.png",

        },
        "新北市私立民權老人長期照顧中心":{
            "text": "\n\n聯絡電話:02-8667-1477\n地址:新店區民權路88-1號2樓",
            "image_path": "n6.png",

        },
        "新北市私立智英老人長期照護中心":{
            "text": "我們竭盡所能提供您家中的失能長者在生命旅途中，能夠獲得我們中心專業服務人員的愛心、耐心且受到安全、舒適與尊嚴的照顧，如同在家中一般。\n\n聯絡電話:02-2908-3247\n地址:新莊區中正路544號",
            "image_path": "n7.png",

        },
        "新北市私立盛禾老人長期照顧中心":{
            "text": "團隊由資深專業的護理師士、照顧服務員，提供24小時全天侯照護服務。另聘有醫師巡診、社工師、營養師、物理職能治療師，滿足住民全方位的照護需求。本中心接近署立台北醫院、林口長庚醫院及署立樂生分院，就醫轉診便利。\n\n聯絡電話:02-2908-1656\n地址:新莊區雙鳳路119號4樓",
            "image_path": "n8.png",

        }
    }

    # 長照中心
    data = {
        "台北市": [
            "臺北市至善老人安養護中心",
            "臺北市私立永青老人長期照顧中心",
            "臺北市私立天玉老人長期照顧中心",
            "臺北市私立健全老人長期照顧中心",
            "臺北市兆如老人安養護中心",
            "臺北市私立恆安老人長期照顧中心",
            "臺北市私立華安老人長期照護中心",
            "臺北市私立全民老人長期照顧中心",
            "臺北市私立安安老人長期照顧中心"
        ],
        "新北市": [
            "財團法人台灣省私立健順養護中心",
            "新北市私立銀泰老人長期照顧中心",
            "新北市私立心田老人長期照顧中心",
            "新北市私立夏雨老人長期照顧中心",
            "財團法人私立廣恩老人養護中心",
            "新北市私立民權老人長期照顧中心",
            "新北市私立智英老人長期照護中心",
            "新北市私立盛禾老人長期照顧中心"
        ],
    }

    root.mainloop()
