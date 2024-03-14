import { NextResponse } from "next/server";
import { query } from "@/app/lib/db";

export const POST = async (req, res) => {
  let message, status;
  const data = await req.json();
  console.log(data);
  const fullname = data.fullname;
  const email = data.email;
  const password = data.pass;
  const phoneNo = data.phone;
  const state = data.state;
  const city = data.city;
  const wardNo = data.ward_no;

  const user = await query({
    query:
      "INSERT INTO `user`(`fullname`, `email`, `pass`, `phone`, `state`, `city`, `ward_no`) VALUES (?, ?, ?, ?, ?, ?, ?)",
    values: [
      fullname,
      email,
      password,
      phoneNo,
      state,
      city,
      wardNo,

      // Assuming "user" is the role you want to assign
    ],
  });

  if (user.error) {
    message = "Something went Wrong";
    status = 500;
  } else {
    (message = "user added successfully"), (status = 201);
  }
  return NextResponse.json({ message: message }, { status: status });
};
