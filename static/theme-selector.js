function loadTheme() {
	let theme = localStorage.getItem("theme");

	if(theme === "light")
	{
		document.body.style.colorScheme = "light";
		document.getElementById("opt-left").checked = true;
	}

	else if(theme === "dark")
	{
		document.body.style.colorScheme = "dark";
		document.getElementById("opt-right").checked = true;
	}

	else if(theme === "system")
	{
		document.body.style.colorScheme = "light dark";
		document.getElementById("opt-mid").checked = true;
	}

	else
	{
		console.log("Invalid theme!");

		// Fallback to system
		document.body.style.colorScheme = "light dark";
		document.getElementById("opt-mid").checked = true;
	}
}


document.querySelectorAll(".three-toggle input[type=radio]").forEach(r => {
	r.addEventListener("change", function(){
		let theme = r.value;
		console.log(theme);
		
		if(theme === "left")
		{
			document.body.style.colorScheme = "light";
			localStorage.setItem("theme", "light");
		}

		else if(theme === "middle")
		{
			document.body.style.colorScheme = "light dark";
			localStorage.setItem("theme", "system");
		}

		else if(theme === "right")
		{
			document.body.style.colorScheme = "dark";
			localStorage.setItem("theme", "dark");
		}

		else
		{
			console.log("Invalid theme!");
		}

	})
});