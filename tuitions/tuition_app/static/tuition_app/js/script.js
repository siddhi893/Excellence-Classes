document.addEventListener('DOMContentLoaded', function() {
    // Use name selectors with fallback to id selectors
    const form = document.getElementById('registration-form');
    const standard = document.querySelector('[name="standard"]') || document.getElementById('id_standard');
    const board = document.querySelector('[name="board"]') || document.getElementById('id_board');
    const subject = document.querySelector('[name="subject"]') || document.getElementById('id_subject');
    const school = document.querySelector('[name="school"]') || document.getElementById('id_school');
    const branch = document.querySelector('[name="branch"]') || document.getElementById('id_branch');
    const fees = document.querySelector('[name="fees"]') || document.getElementById('id_fees');
    const darkModeToggle = document.getElementById('dark-mode');
    const nameField = document.querySelector('[name="name"]') || document.getElementById('id_name');
    const phoneField = document.querySelector('[name="phone"]') || document.getElementById('id_phone');
    const fathernameField = document.querySelector('[name="father_name"]') || document.getElementById('id_father_name');
    const fatherphoneField = document.querySelector('[name="father_phone"]') || document.getElementById('id_father_phone');
    const fatheroccupationField = document.querySelector('[name="occupation"]') || document.getElementById('id_occupation');
    const addressField = document.querySelector('[name="address"]') || document.getElementById('id_address');
    const paymentMode = document.querySelector('[name="payment_mode"]') || document.getElementById('id_payment_mode');
    const paymentProof = document.querySelector('[name="payment_proof"]') || document.getElementById('id_payment_proof');
    const schoolDropdownField = document.getElementById('school-dropdown-field');
    const schoolTextField = document.getElementById('school-text-field');
    const hscSchoolInput = document.getElementById('hsc-school');

    // Log elements to debug
    console.log('branch:', branch);
    console.log('school:', school);
    console.log('hscSchoolInput:', hscSchoolInput);

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
        if (!standard || !board || !subject || !school || !branch || !fees) {
            console.error('One or more form elements are missing');
            return;
        }

        const stdVal = standard.value;
        const boardVal = board.value;
        const branchVal = branch.value;
        const subjectVal = subject.value;

        const currentName = nameField ? nameField.value : '';
        const currentPhone = phoneField ? phoneField.value : '';
        const currentFatherName = fathernameField ? fathernameField.value : '';
        const currentFatherPhone = fatherphoneField ? fatherphoneField.value : '';
        const currentFatherOccupation = fatheroccupationField ? fatheroccupationField.value : '';
        const currentAddress = addressField ? addressField.value : '';

        if (stdVal !== form.dataset.lastStandard) {
            board.value = '';
            subject.value = '';
            fees.value = '';
            form.dataset.lastStandard = stdVal;
            form.dataset.lastBoard = '';
        }

        if (!boardVal || stdVal !== form.dataset.lastStandard) {
            board.innerHTML = '<option value="">-- Select Board --</option>';
            if (stdVal === '12') {
                addOption(board, 'HSC', 'HSC');
            } else {
                addOption(board, 'CBSE', 'CBSE');
                addOption(board, 'SSC', 'SSC');
            }
        }

        if (!subjectVal || stdVal !== form.dataset.lastStandard) {
            subject.innerHTML = '<option value="">-- Select Subject --</option>';
            if (stdVal === '12') {
                addOption(subject, 'English', 'English');
            } else {
                addOption(subject, 'English', 'English');
                addOption(subject, 'Social Studies', 'Social Studies');
                addOption(subject, 'Both', 'Both');
            }
        }

        if (stdVal && boardVal && (stdVal !== form.dataset.lastStandard || boardVal !== form.dataset.lastBoard)) {
            if (stdVal === '12' && boardVal === 'HSC') {
                schoolDropdownField.style.display = 'none';
                schoolTextField.style.display = 'block';
                school.value = hscSchoolInput ? (hscSchoolInput.value || 'NA') : 'NA';
            } else {
                schoolDropdownField.style.display = 'block';
                schoolTextField.style.display = 'none';
                if (hscSchoolInput) hscSchoolInput.value = '';
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
            }
            form.dataset.lastBoard = boardVal;
        }

        if (stdVal === '12' && boardVal === 'HSC' && hscSchoolInput) {
            school.value = hscSchoolInput.value || 'NA';
        }

        if (nameField) nameField.value = currentName;
        if (phoneField) phoneField.value = currentPhone;
        if (fathernameField) fathernameField.value = currentFatherName;
        if (fatherphoneField) fatherphoneField.value = currentFatherPhone;
        if (fatheroccupationField) fatheroccupationField.value = currentFatherOccupation;
        if (addressField) addressField.value = currentAddress;

        if (stdVal && boardVal && branchVal && subjectVal) {
            let baseFee = feeStructure[branchVal]?.[boardVal]?.[stdVal] || 0;
            fees.value = (subjectVal === 'Both' && stdVal !== '12') ? baseFee * 2 : baseFee;
            console.log(`Fees set to: ${fees.value}`);
        } else {
            fees.value = '';
        }

        const paymentModeVal = paymentMode ? paymentMode.value : '';
        if (paymentModeVal === 'cash') {
            if (paymentProof) {
                paymentProof.disabled = true;
                paymentProof.value = '';
                paymentProof.required = false;
            }
        } else {
            if (paymentProof) {
                paymentProof.disabled = false;
                paymentProof.required = true;
            }
        }

        checkFormCompletion();
    }

    function checkFormCompletion() {
        const requiredFields = [
            nameField, phoneField, fathernameField, fatherphoneField, 
            fatheroccupationField, addressField, standard, board, 
            subject, branch, school, fees, paymentMode
        ].filter(field => field !== null); // Remove null fields
        
        const allFieldsFilled = requiredFields.every(field => {
            return field.value && field.value.trim() !== '';
        });

        const paymentValid = paymentMode && (paymentMode.value === 'cash' || 
                           (paymentMode.value === 'online' && paymentProof && paymentProof.files.length > 0));

        submitButton.disabled = !(allFieldsFilled && paymentValid);
    }

    function addOption(select, value, text) {
        const option = document.createElement('option');
        option.value = value;
        option.text = text;
        select.appendChild(option);
    }

    standard.addEventListener('change', updateForm);
    board.addEventListener('change', updateForm);
    subject.addEventListener('change', updateForm);
    branch.addEventListener('change', updateForm);
    paymentMode.addEventListener('change', updateForm);
    if (paymentProof) paymentProof.addEventListener('change', checkFormCompletion);
    if (hscSchoolInput) hscSchoolInput.addEventListener('input', updateForm);

    const allFields = form.querySelectorAll('input, select, textarea');
    allFields.forEach(field => {
        field.addEventListener('input', checkFormCompletion);
        field.addEventListener('change', checkFormCompletion);
    });

    darkModeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        this.textContent = document.body.classList.contains('dark-mode') ? '☀️' : '🌙';
    });

    console.log('Initial form update');
    updateForm();
});