from tkinter import *
from functools import *
from PIL import Image
mainwin=Tk()
mainwin.geometry("800x500")

mainwin.title("IMAGE PROCESSING SOFTWARE")

def nextfun():
    catalogwin=Tk()
    catalogwin.geometry("700x400")
    
    def imgrotate():
        rotatewin=Tk()
        rotatewin.geometry("650x400")
        
        def finallyrotate():
    
            one=eone.get()
            two=etwo.get()
            three=int(edegree.get())
            
            if one!="" and two!="":
                im=Image.open(one)
                im=im.rotate(three)
                im.save(two)
                statuslb.config(text="Status: Completed")
            else:
                statuslb.config(text="Status: Error")
           
        
        rotatewin.title("IMAGE PROCESSING SOFTWARE")
        lbone=Label(rotatewin,text="Note: Please put your image in that folder where you save this software").place(x=20,y=80)
        lbtwo=Label(rotatewin,text="Please enter name of your image")
        
        eone=Entry(rotatewin)
        eone.place(x=20,y=100)
        
        lbdegree=Label(rotatewin,text="Enter degree").place(x=20,y=130)
        edegree=Entry(rotatewin)
        edegree.place(x=20,y=160)
        
        lbthree=Label(rotatewin,text="Note: After Rotation your new generated image will save in folder where you put this software").place(x=20,y=190)
        lbfourth=Label(rotatewin,text="please enter any name which you want to give to new generated image in below field").place(x=20,y=230)
        etwo=Entry(rotatewin)
        etwo.place(x=20,y=260)
        
        rotationbtn=Button(rotatewin,text="Rotate Image",height=2,width=15,command=finallyrotate).place(x=20,y=290)
        statuslb=Label(rotatewin,text="Status:")
        statuslb.place(x=20,y=330)
        rotatewin.mainloop()
        
    def thumb():
        thumbwin=Tk()
        thumbwin.geometry("650x400")
        thumbwin.title("IMAGE PROCESSING SOFTWARE")
        
        def finallythumb():
            onethumb=entthumbone.get()
            twothumb=entthumbtwo.get()
            threethumb=int(entthumbthree.get())
            fourthumb=int(entthumbfour.get())
            
            if onethumb!="" and twothumb!="":
                image = Image.open(onethumb)
                image.thumbnail((threethumb,fourthumb))
                image.save(twothumb)
                statusthumb.config(text="Status: Completed")
            else:
                statusthumb.config(text="Status: Error")
        
        lbone=Label(thumbwin,text="Note: Please put your image in that folder where you save this software").place(x=20,y=20)
        lbtwo=Label(thumbwin,text="Please enter name of your image").place(x=20,y=50)
        
        entthumbone=Entry(thumbwin)
        entthumbone.place(x=20,y=80)
        
        lbthree=Label(thumbwin,text="Enter coordinates")
        lbthree.place(x=20,y=110)
        
        entthumbthree=Entry(thumbwin)
        entthumbthree.place(x=20,y=140)
        
        entthumbfour=Entry(thumbwin)
        entthumbfour.place(x=20,y=170)
        
        lbthree=Label(thumbwin,text="Note: After Rotation your new generated image will save in folder where you put this software").place(x=20,y=200)
        lbfourth=Label(thumbwin,text="please enter any name which you want to give to new generated image in below field").place(x=20,y=230)
        
        entthumbtwo=Entry(thumbwin)
        entthumbtwo.place(x=20,y=260)
        
        
        thumbbtn=Button(thumbwin,text="Thumbnail Image",height=2,width=15,command=finallythumb).place(x=20,y=290)
        statusthumb=Label(thumbwin,text="Status:")
        statusthumb.place(x=20,y=340)
        thumbwin.mainloop()
        
    def blur():
        blurwin=Tk()
        blurwin.geometry("650x400")
        blurwin.title("IMAGE PROCESSING SOFTWARE")
        
        def minblur():
            first=entblurone.get()
            second=entblurtwo.get()
            if first!="" and second!="":
                from PIL import Image, ImageFilter

                OriImage = Image.open(first)
                OriImage.show()
                blurImage = OriImage.filter(ImageFilter.BLUR)
                blurImage.show()

                blurImage.save(second)
                statusblur.config(text="Status: Completed")
                return None
        
        def midblur():
            first=entblurone.get()
            second=entblurtwo.get()
            if first!="" and second!="":
                from PIL import Image, ImageFilter

                OriImage = Image.open(first)
                OriImage.show()
                blurImage = OriImage.filter(ImageFilter.BoxBlur(5))
                blurImage.show()

                blurImage.save(second)
                statusblur.config(text="Status: Completed")
                return None 

        def highblur():
            first=entblurone.get()
            second=entblurtwo.get()
            if first!="" and second!="":
                from PIL import Image, ImageFilter

                OriImage = Image.open(first)
                OriImage.show()
                blurImage = OriImage.filter(ImageFilter.GaussianBlur(5))
                blurImage.show()

                blurImage.save(second)
                statusblur.config(text="Status: Completed")
                return None 
                        
        lbone=Label(blurwin,text="Note: Please put your image in that folder where you save this software").place(x=20,y=20)
        lbtwo=Label(blurwin,text="Please enter name of your image").place(x=20,y=50)
        
        entblurone=Entry(blurwin)
        entblurone.place(x=20,y=80)
        
        lbthree=Label(blurwin,text="Note: After Rotation your new generated image will save in folder where you put this software").place(x=20,y=110)
        lbfourth=Label(blurwin,text="please enter any name which you want to give to new generated image in below field").place(x=20,y=140)
        
        entblurtwo=Entry(blurwin)
        entblurtwo.place(x=20,y=170)
        
       
        
        minblurbtn=Button(blurwin,text="Minimum Blur",height=2,width=15,command=minblur).place(x=20,y=200)
        midblurbtn=Button(blurwin,text="Medium Blur",height=2,width=15,command=midblur).place(x=20,y=230)
        highblurbtn=Button(blurwin,text="High Blur",height=2,width=15,command=highblur).place(x=20,y=260)
        statusblur=Label(blurwin,text="Status:")
        statusblur.place(x=20,y=300)
        
        blurwin.mainloop()
    
    
    def flip():
        flipwin=Tk()
        flipwin.geometry("650x400")
        flipwin.title("IMAGE PROCESSING SOFTWARE")
        
        def lefttoright():
        
            one=entflipone.get()
            two=entfliptwo.get()
            
            from PIL import Image

            imageObject = Image.open(one)
            hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
            hori_flippedImage.save(two)
            statusflip.config(text="Status: Flipped Successfully")
        def toptobottom():
        
            one=entflipone.get()
            two=entfliptwo.get()
            
            from PIL import Image

            imageObject = Image.open(one)
            hori_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
            hori_flippedImage.save(two)
            statusflip.config(text="Status: Flipped Successfully")

        def nintydegree():
        
            one=entflipone.get()
            two=entfliptwo.get()
            
            from PIL import Image

            imageObject = Image.open(one)
            hori_flippedImage = imageObject.transpose(Image.ROTATE_90)
            hori_flippedImage.save(two)
            statusflip.config(text="Status: Flipped Successfully")
            
        lbone=Label(flipwin,text="Note: Please put your image in that folder where you save this software").place(x=20,y=20)
        lbtwo=Label(flipwin,text="Please enter name of your image").place(x=20,y=50)
        
        entflipone=Entry(flipwin)
        entflipone.place(x=20,y=80)
        
        lbthree=Label(flipwin,text="Note: After Rotation your new generated image will save in folder where you put this software").place(x=20,y=110)
        lbfourth=Label(flipwin,text="please enter any name which you want to give to new generated image in below field").place(x=20,y=140)
        
        entfliptwo=Entry(flipwin)
        entfliptwo.place(x=20,y=170)
        
        btnfirst=Button(flipwin,text="Flip Left to Right",command=lefttoright).place(x=20,y=200)
        btnsecond=Button(flipwin,text="Flip Top to Bottom",command=toptobottom).place(x=140,y=200)
        btnthird=Button(flipwin,text="Rotate 90 degree",command=nintydegree).place(x=260,y=200)
        statusflip=Label(flipwin,text="Status:")
        statusflip.place(x=20,y=240)
        flipwin.mainloop()
        
    
  
        
    def filtering():
        filterwin=Tk()
        filterwin.geometry("650x400")
        filterwin.title("IMAGE PROCESSING SOFTWARE")
        
        def finallycontour():
        
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(CONTOUR)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        
        def finallydetail():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(DETAIL)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        def finallyedgeenhance():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filte(EDGE_ENHANCE)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        def finallyemboss():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(EMBOSS)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        def finallyfindedges():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(FIND_EDGES)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        def finallysharp():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(SMOOTH)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        def finallysmooth():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(SMOOTH_MORE)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
        def finallysmoothmore():
            one=entonefilter.get()
            two=enttwofilter.get()
        
            from PIL import Image, ImageFilter

            from PIL.ImageFilter import (
            BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
            EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
            )
            img = Image.open(one)
            img1 = img.filter(SHARPEN)
            img1.save(two)
            img1.show()
            statusfilter.config(text="Status: Successfully Filtered")
            
        lbone=Label(filterwin,text="Note: Please put your image in that folder where you save this software").place(x=20,y=80)
        lbtwo=Label(filterwin,text="Please enter name of your image").place(x=20,y=110)
        
        entonefilter=Entry(filterwin)
        entonefilter.place(x=20,y=140)
        
        lbthree=Label(filterwin,text="Note: After Rotation your new generated image will save in folder where you put this software").place(x=20,y=170)
        lbfourth=Label(filterwin,text="please enter any name which you want to give to new generated image in below field").place(x=20,y=200)
        
        enttwofilter=Entry(filterwin)
        enttwofilter.place(x=20,y=230)
        
        btn=Button(filterwin,text="Contour",command=finallycontour).place(x=20,y=260)
        btn=Button(filterwin,text="Detail",command=finallydetail).place(x=80,y=260)
        btn=Button(filterwin,text="Edge Enhance",command=finallyedgeenhance).place(x=130,y=260)
        btn=Button(filterwin,text="Emboss",command=finallyemboss).place(x=220,y=260)
        btn=Button(filterwin,text="Find Edges",command=finallyfindedges).place(x=280,y=260)
        btn=Button(filterwin,text="Sharpen",command=finallysharp).place(x=350,y=260)
        btn=Button(filterwin,text="Smooth",command=finallysmooth).place(x=410,y=260)
        btn=Button(filterwin,text="Smooth More",command=finallysmoothmore).place(x=480,y=260)
        statusfilter=Label(filterwin,text="Status:")
        statusfilter.place(x=20,y=290)
        filterwin.mainloop()
        
    
    catalogwin.title("IMAGE PROCESSING SOFTWARE")
    lb=Label(catalogwin,text="Please Select What you want to do?").place(x=280,y=20)
    rotationbtn=Button(catalogwin,text="IMAGE ROTATION",command=imgrotate).place(x=320,y=50)
    thumbnailbtn=Button(catalogwin,text="THUMBNAIL CREATION",command=thumb).place(x=320,y=80)
    blurbtn=Button(catalogwin,text="IMAGE BLURRING",command=blur).place(x=320,y=110)
    
    flippingbtn=Button(catalogwin,text="IMAGE FLIPPING",command=flip).place(x=320,y=140)
 
    filteringbtn=Button(catalogwin,text="IMAGE FILTERING",command=filtering).place(x=320,y=170)
  
    
    catalogwin.mainloop()

nxtbtn=Button(mainwin,text="NEXT->>",fg="white",
bg="blue",height=2,width=10,command=nextfun).place(x=380,y=200)


namelb=Label(mainwin,font=40,text="This Software is created by 'Mr. Hemant Vaishnav'").place(x=210,y=350)
mainwin.mainloop()