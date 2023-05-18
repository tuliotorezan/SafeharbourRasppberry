const axios = require('axios');
 const fs = require('fs');
 
async function sendPicture() {
   try {
 	const fileContent = fs.readFileSync('LatestPicture.jpg');
 	const base64Image = Buffer.from(fileContent).toString('base64');
 
	const response = await axios.post('http://ec2-35-175-185-229.compute-1.amazonaws.com/getPicture', {
   	image: base64Image,
 	});
 
	console.log('Picture sent successfully:', response.data);
   } catch (error) {
 	console.error('Error sending picture:', error.message);
   }
 }
 
// Send a picture every 10 minutes
 setInterval(sendPicture, 10 * 60 * 3);
