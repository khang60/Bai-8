import streamlit as st
with st.sidebar:
  image = 'assets/0934_3.jpg'
  st.image(image,caption = "Den vau")
  st.write('Họ và tên: Nguyễn Đức Cường')
  st.write('Nghệ danh: Đen Vâu')
  st.write('Đen Vâu là một nam rapper người Việt Nam. ')

st.title('Bài hát yêu thích ')
st.write('Ngày Khác Lạ')
sound = open('assets/NgayKhacLa-DenDJGiangPhamTripleD-5393909.mp3', 'rb')
st.audio(sound, format = 'audio/mp3')
st.write('Cho Tôi Lang Thang')
sound = open('assets/ChoToiLangThang-NgotDen-4817311.mp3', 'rb')
st.audio(sound, format = 'audio/mp3')
st.title('MV yêu thích')
st.write('Mang tiền về cho mẹ')
video = 'https://www.youtube.com/watch?v=UVbv-PJXm14'
st.video(video, format = 'video/mp4')
st.write('Đi về nhà')
video = 'https://www.youtube.com/watch?v=vTJdVE_gjI0'
st.video(video, format = 'video/mp4')