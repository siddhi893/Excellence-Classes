// tuition_app/static/tuition_app/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registration-form');
    const standard = document.querySelector('[name="standard"]');
    const board = document.querySelector('[name="board"]');
    const subject = document.querySelector('[name="subject"]');
    const school = document.querySelector('[name="school"]');
    const branch = document.querySelector('[name="branch"]');
    const fees = document.querySelector('[name="fees"]');
    const darkModeToggle = document.getElementById('dark-mode');
    const nameField = document.querySelector('[name="name"]');
    const phoneField = document.querySelector('[name="phone"]');
    const addressField = document.querySelector('[name="address"]');
    const paymentMode = document.querySelector('[name="payment_mode"]');
    const paymentProof = document.querySelector('[name="payment_proof"]');
    const submitButton = form.querySelector('button[type="submit"]');

    // Fees calculation logic
    const feeStructure = {
        'Gulmohar': {
            'CBSE': { '8': 7500, '9': 8000, '10': 9000 },
            'SSC': { '8': 7500, '9': 4000, '10': 5000 },
            'HSC': { '12': 7000 }
        },
        'Market Yard': {
            'CBSE': { '8': 7500, '9': 9000, '10': 10000 },
            'SSC': { '8': 7500, '9': 4000, '10': 5000 },
            'HSC': { '12': 7000 }
        }
    };

    function updateForm() {
        const stdVal = standard.value;
        const boardVal = board.value;
        const branchVal = branch.value;
        const subjectVal = subject.value;
        const paymentModeVal = paymentMode.value;

        // Store current values of name, phone, and address before any changes
        const currentName = nameField.value;
        const currentPhone = phoneField.value;
        const currentAddress = addressField.value;

        // Reset dependent fields when standard changes
        if (stdVal !== form.dataset.lastStandard) {
            board.value = ''; // Reset to placeholder
            subject.value = ''; // Reset to placeholder
            school.value = ''; // Reset to placeholder
            fees.value = '';
            form.dataset.lastStandard = stdVal;
            form.dataset.lastBoard = ''; // Reset lastBoard to force school update
        }

        // Update board options with placeholder
        board.innerHTML = '<option value="">-- Select Board --</option>';
        if (stdVal === '12') {
            addOption(board, 'HSC', 'HSC');
        } else {
            addOption(board, 'CBSE', 'CBSE');
            addOption(board, 'SSC', 'SSC');
        }
        if (boardVal && board.querySelector(`option[value="${boardVal}"]`)) {
            board.value = boardVal;
        } else {
            board.value = '';
        }

        // Update subject options with placeholder
        subject.innerHTML = '<option value="">-- Select Subject --</option>';
        if (stdVal === '12') {
            addOption(subject, 'English', 'English');
        } else {
            addOption(subject, 'English', 'English');
            addOption(subject, 'Social Studies', 'Social Studies');
            addOption(subject, 'Both', 'Both');
        }
        if (subjectVal && subject.querySelector(`option[value="${subjectVal}"]`)) {
            subject.value = subjectVal;
        } else {
            subject.value = '';
        }

        // Update school options with placeholder (only if standard or board changes)
        if (stdVal !== form.dataset.lastStandard || boardVal !== form.dataset.lastBoard) {
            school.innerHTML = '<option value="">-- Select School --</option>';
            if (stdVal === '12') {
                addOption(school, 'NA', 'Not Applicable');
            } else if (boardVal === 'CBSE') {
                ['Saint Michael School', 'Orchid School', 'Sai Angel School', 
                 'Icon Public School', 'Takshila School', 'Podar School']
                .forEach(s => addOption(school, s, s));
            } else if (boardVal === 'SSC') {
                ['Auxilium Convent School', 'Sacred Heart Convent School', 
                 'Ashokbhau Firodia School', 'Athare Patil School']
                .forEach(s => addOption(school, s, s));
            }
            form.dataset.lastBoard = boardVal;
        }

        // Restore name, phone, and address values
        nameField.value = currentName;
        phoneField.value = currentPhone;
        addressField.value = currentAddress;

        // Calculate fees
        if (stdVal && boardVal && branchVal && subjectVal) {
            let baseFee = feeStructure[branchVal]?.[boardVal]?.[stdVal] || 0;
            fees.value = subjectVal === 'Both' ? baseFee * 2 : baseFee;
        } else {
            fees.value = '';
        }

        // Handle payment mode logic
        if (paymentModeVal === 'cash') {
            paymentProof.disabled = true;
            paymentProof.value = ''; // Clear any uploaded file
            submitButton.disabled = false; // Enable submit for cash
        } else if (paymentModeVal === 'online') {
            paymentProof.disabled = false;
            submitButton.disabled = !paymentProof.files.length; // Disable submit until file uploaded
        } else {
            paymentProof.disabled = false;
            submitButton.disabled = false; // Default state when no payment mode selected
        }
    }

    function addOption(select, value, text) {
        const option = document.createElement('option');
        option.value = value;
        option.text = text;
        select.appendChild(option);
    }

    // Event listeners
    standard.addEventListener('change', updateForm);
    board.addEventListener('change', updateForm);
    subject.addEventListener('change', updateForm);
    branch.addEventListener('change', updateForm);
    paymentMode.addEventListener('change', function() {
        updateForm();
        // Additional check for online payment when mode changes
        if (this.value === 'online') {
            submitButton.disabled = !paymentProof.files.length;
        }
    });
    paymentProof.addEventListener('change', function() {
        if (paymentMode.value === 'online') {
            submitButton.disabled = !this.files.length;
        }
    });

    // Dark mode toggle
    darkModeToggle.addEventListener('click', function() {  // Changed from 'change' to 'click' for button
        document.body.classList.toggle('dark-mode');
        // Toggle between moon and sun emojis
        if (document.body.classList.contains('dark-mode')) {
            darkModeToggle.textContent = '☀️'; // Sun emoji for light mode
        } else {
            darkModeToggle.textContent = '🌙'; // Moon emoji for dark mode
        }
    });

    // Initial update
    updateForm();
});